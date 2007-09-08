from logging import DEBUG
import os
from os.path import isdir
import shutil
import tempfile
from cStringIO import StringIO as cStringIO
from StringIO import StringIO

from zope.interface import implements

from plone.transforms.interfaces import ICommandTransform
from plone.transforms.log import log
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import TransformResult
from plone.transforms.utils import bin_search


class CommandTransform(PersistentTransform):
    """A persistent transform which runs a transform based on a command line
    tool.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICommandTransform, CommandTransform)
      True
    """

    implements(ICommandTransform)

    name = u'plone.transforms.transform.CommandTransform'
    title = _(u'title_skeleton_command_transform',
              default=u'A skeleton command transform.')
    description = None

    inputs = (None, )
    output = None

    available = False

    command = None
    args = None

    def __init__(self):
        super(CommandTransform, self).__init__()
        if self.command is None:
            log(DEBUG, "There was no command given for the %s transform." %
                        self.name)
        else:
            if bin_search(self.command):
                self.available = True
            else:
                log(DEBUG, "The binary %s could not be found, while trying "
                           "to use the %s transform." % (self.command, self.name))

    def write(self, fd, data):
        # write data to tmp using a file descriptor
        firstchunk = data.next()
        if isinstance(firstchunk, unicode):
            self.write_text(fd, firstchunk, data)
        else:
            self.write_binary(fd, firstchunk, data)

    def write_binary(self, fd, firstchunk, data):
        os.write(fd, firstchunk)
        for chunk in data:
            os.write(fd, chunk)

    def write_text(self, fd, firstchunk, data):
        os.write(fd, firstchunk.encode('utf-8'))
        for chunk in data:
            os.write(fd, chunk.encode('utf-8')) 

    def initialize_tmpfile(self, data, directory=None):
        """Create a temporary file and copy input into it.
        Returns the path of the tmp file.

        The temporary directory in which the file is being created can
        optionally be specified via the directory argument.
        """
        if directory is None:
            fd, tmpfilepath = tempfile.mkstemp(text=False)
        else:
            fd, tmpfilepath = tempfile.mkstemp(text=False, dir=directory)
        # write data to tmp using a file descriptor
        self.write(fd, data)
        # close it so the other process can read it
        os.close(fd)
        return tmpfilepath

    # XXX Provide more control arguments, like %(outfile)s
    def prepare_transform(self, data, infile_data_suffix=False):
        """
        The method takes some data in one of the input formats and returns
        a TransformResult with data in the output format.
        """
        result = TransformResult(None)
        try:
            tmpdirpath = tempfile.mkdtemp()
            tmpfilepath = self.initialize_tmpfile(data, directory=tmpdirpath)
            if infile_data_suffix:
                primaryname = os.path.basename(tmpfilepath) + infile_data_suffix

            commandline = 'cd "%s" && %s %s' % (
                tmpdirpath, self.command, self.args)

            commandline = commandline % { 'infile' : tmpfilepath }
            if os.name=='posix':
                # TODO: tbenita suggests to remove 1>/dev/null as some commands
                # return result in flow. Maybe turn this into another subobject
                # commandline = commandline + ' 2>error_log'
                commandline = commandline + ' 2>error_log 1>/dev/null'

            os.system(commandline)

            for tmpfile in os.listdir(tmpdirpath):
                tmp = os.path.join(tmpdirpath, tmpfile)
                # Exclude the original file and the error_log from the result
                if tmp == tmpfilepath:
                    continue
                fd = file(tmp, 'rb')
                # Should we use the infile as the primary output?
                if infile_data_suffix and primaryname == tmpfile:
                    result.data = StringIO()
                    result.data.writelines(fd)
                    result.data.seek(0)
                elif tmp.endswith('error_log'):
                    result.errors = fd.read()
                else:
                    sub = cStringIO()
                    sub.writelines(fd)
                    sub.seek(0)
                    result.subobjects[tmpfile] = sub
                fd.close()
                os.unlink(tmp)
        finally:
            if isdir(tmpdirpath):
                shutil.rmtree(tmpdirpath)

        return result

    def transform(self, data):
        """Returns the transform result."""
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data)
        return result
