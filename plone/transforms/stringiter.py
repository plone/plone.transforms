from cStringIO import StringIO

class StringIter(object):
    """Provides an initialze only version of a StringIO class, which
    accepts only Unicode input but stores it internally as utf-8 in a
    cStringIO for better performance.

    Retrieving the value is only possible via the iterator protocol.
    """

    def __init__(self, v):
        self.v = StringIO(v.encode('utf-8'))
        self.vn = self.v.next

    def __iter__(self):
        return self

    def next(self):
        return unicode(self.vn(), 'utf-8')
