from string import ascii_lowercase, ascii_uppercase


class Logger(object):   # this is a standard logger.
    def __init__(self, logger=print):
        self.logger = logger
    def log(*args):
        self.logger(*args)


def shift_char(char, dx):
    """
    This function returns the char obtained after displacement of dx from char.
    """
    if not isinstance(char, str) or len(char) != 1 :
        raise ValueError("Char is a one length string.")
    
    if char.isupper():
        charset = ascii_uppercase
    else:
        charset = ascii_lowercase
    base_idx = charset.index(char)
    return charset[ (base_idx + dx) % 26 ]
