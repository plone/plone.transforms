from cStringIO import StringIO

class StringIter(object):
    """Provides an initialze only version of a StringIO class, which
    accepts Unicode and utf-8 encoded input, stores it internally as utf-8 in a
    cStringIO for better performance and always outputs Unicode.

    Retrieving the value is only possible via the iterator protocol.
    """

    def __init__(self, v):
        if isinstance(v, unicode):
            self.v = StringIO(v.encode('utf-8'))
        else:
            self.v = StringIO(v)
        self.vn = self.v.next

    def __iter__(self):
        return self

    def next(self):
        return unicode(self.vn(), 'utf-8')
