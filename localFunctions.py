import random
import string

def generateRandomness(l):
    rndString = ''.join(random.choice(string.ascii_lowercase + ' ') for x in range(l))
    return rndString

def generateFilename(l,fnExt):
    fname = ''.join(random.choice(string.ascii_lowercase) for x in range(l))
    return fname + "." + fnExt

def generateDirname(l):
    dname = ''.join(random.choice(string.ascii_lowercase) for x in range(l))
    return dname

def humanreadableNumber(n):
    if n < 999999:
        return str(format(n,','))
    elif n < 999999999:
        return str(format(round(n/1000000,1),',')) + " million"
    elif n < 999999999999:
        return str(format(round(n/1000000000,1),',')) + " billion"
    else:
        return str(format(n,'E'))

def humanreadableFilesize(n):
    if n <= 1000:
        return str(n) + "KB"
    elif n <= 1000000:
        return str(round(n/1000,2)) + "MB"
    elif n <= 1000000000:
        return str(round(n/1000000,2)) + "GB"
    else:
        return str(round(n/1000000000,2)) + "TB"
