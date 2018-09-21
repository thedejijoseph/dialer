# so ive been thnn thinking about this keypad thingy on phones and how you can find contacts with names or phone numbers...

import sys
import extract

class ParseError(Exception):
    pass

valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+"
