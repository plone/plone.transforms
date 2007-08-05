import os
import sys

# Use the PATH environment variable to look for binaries
BIN_SEARCH_PATH = [path for path in os.environ['PATH'].split(os.pathsep)
                   if os.path.isdir(path)]

# Windows executes binaries with some suffixes
BIN_EXTENSIONS = ('', )
if sys.platform.startswith('win32'):
   BIN_EXTENSIONS = ('.exe', '.com', '.bat', )

# We need to read and execute the binary
BIN_ACCESS_MODE = os.R_OK | os.X_OK


def bin_search(binary):
    """Search the BIN_SEARCH_PATH for a given binary returning its fullname or
    returns None.
    """
    for path in BIN_SEARCH_PATH:
        for ext in BIN_EXTENSIONS:
            pathbin = os.path.join(path, binary) + ext
            if os.access(pathbin, BIN_ACCESS_MODE):
                return pathbin
    return None


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

