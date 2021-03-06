import random
import string
import sys #for progress bar
import math

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
    millnames = ['',' Thousand',' Million',' Billion',' Trillion']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


def humanreadableFilesize(bytes):
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    if bytes == 0:
        return '0 Byte'

    i = int(math.floor(math.log(bytes) / math.log(1024)))
    if i > len(sizes):
        
        return str(round(bytes / math.pow(1024, i),2 )) + ' whatever' #just to return something funny to the user if the number is totally out of scope
    else:
        return str(round(bytes / math.pow(1024, i),2 )) + ' ' + sizes[i]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calcHowmanyfolders(numFolders, subdirLevel, numFiles, kb):
    foldersOnthislevel = numFolders         #level1
    totalFolders = foldersOnthislevel
    for x in range(1,subdirLevel+1):        #need to add 1 as range does not include last number
        foldersOnthislevel = foldersOnthislevel * numFolders
        totalFolders += foldersOnthislevel

    totalFiles = totalFolders * numFiles
    totalkb = totalFiles * kb
    
    run = input("\nA total of " + humanreadableNumber(totalFolders) + " folders and " + humanreadableNumber(totalFiles) + " files that will take appr " + humanreadableFilesize(totalkb) + " of diskspace will be created. Ok to continue (Y/N)?")
    
    if run != 'Y' and run != 'y':
        exit()
    print()
    print()
    return totalFiles   #we need this to show the progress bar

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def progress(count, total, status=''):
    percents = round(100.0 * count / float(total), 1)

    sys.stdout.write('%s%s ...%s\r' % (percents, '%', status))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def getNumericValue(prompt, type = 'int'):
    while True:
        try:
            if type == 'int':
                value = int(input(prompt))
            elif type == 'float':
                value = float(input(prompt))
        except ValueError:
            print("Please input a numeric value only (no decimals)\n")
            continue

        if value < 0:
            print("Please input a positive numeric value only.\n")
            continue
        else:
            break
    return value