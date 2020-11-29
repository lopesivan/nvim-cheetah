import sys
import vim
import os
from .buffer import Buffer

class Redirect(object):
    """docstring for Redirect"""
    def __init__(self, buf):
        self.buf = buf or vim.current.window.buffer

        try:
            sys._stdout
        except:
            sys._stdout = sys.stdout

        sys.stdout = Buffer(buf)
