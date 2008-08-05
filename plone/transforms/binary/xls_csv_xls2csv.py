from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.chain import PersistentTransformChain
from plone.transforms.stringiter import StringIter


class XlsCsvXls2csvCommandTransform(PipeTransform):
    """A transform which transforms xls into HTML."""

    title = _(u'title_xls_csv_xls2csv_transform',
        default=u'Xls to CSV transform.')

    inputs = ("application/vnd.ms-excel", "application/msexcel", )
    output = "text/comma-separated-values"

    command = 'xls2csv'
    args = " %(infile)s > %(infile)s.csv "

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data, infile_data_suffix='.csv')
        text = ''.join(result.data)
        text = text.decode('utf-8', 'ignore')
        result.data = StringIter(text)
        return result


class XlsTextTransform(PersistentTransformChain):
    """A transform chain which transforms xls into text."""

    title = _(u'title_xls_text_transform',
        default=u'XLS to Text only transform')

    def __init__(self):
        super(XlsTextTransform, self).__init__()
        self.append(('plone.transforms.interfaces.IPipeTransform',
                     u'plone.transforms.binary.xls_csv_xls2csv.XlsCsvXls2csvCommandTransform'))
        self.append(('plone.transforms.interfaces.ITransform',
                     u'plone.transforms.text.csv_text.CsvTextTransform'))
