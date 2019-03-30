from string import ascii_lowercase, ascii_uppercase


class Logger(object):   # this is a standard logger.
    def __init__(self, logger=print):
        self.logger = logger
    def log(*args):
        self.logger(*args)


def _egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = _egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


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
