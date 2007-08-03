# This method was taken from Products.CMFDefault.utils.py released under the
# ZPL 2.1 license.

def html_bodyfinder(text):
    """ Return body or unchanged text if no body tags found.
    """
    lowertext = text.lower()
    bodystart = lowertext.find('<body')
    if bodystart == -1:
        return text
    bodystart = lowertext.find('>', bodystart) + 1
    if bodystart == 0:
        return text
    bodyend = lowertext.rfind('</body>', bodystart)
    if bodyend == -1:
        return text
    return text[bodystart:bodyend]
