from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.stringiter import StringIter


class PythonHtmlTransform(PipeTransform):
    """A transform which transforms Python code into HTML with code syntax
    highlighting.
    """

    title = _(u'title_python_html_transform',
        default=u'Python to HTML transform')

    inputs = ("text/x-python", )
    output = "text/html"

    command = 'source-highlight'
    args = "--src-lang=python --out-format=xhtml --no-doc --tab=4"
    use_stdin = True

    def extract_output(self, stdout):
        text = stdout.read().decode('utf-8', 'ignore')
        # Remove the comment header
        text = text[text.find('-->')+3:].strip()
        return StringIter(text)
