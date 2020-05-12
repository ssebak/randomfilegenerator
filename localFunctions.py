import random
import string

ef generateRandomness(l):
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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def createFiles(dirName,filesize,totalFiles):
    global i
    fileName = generateFilename(filenameLength,filenameExtension)
    #filePath = fileName
    filePath = os.path.join(dirName, fileName)
    f = open (filePath,"w")
    rndString = generateRandomness(filesize)
    f.write (rndString)
    f.close()

    progress(i, totalFiles, status='Creating files')
    i += 1

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def createFolder(createinDir,subdirCreated,totalFiles):
    global subdirLevel
    
    for x in range(numDirectories):
        dirName = os.path.join(createinDir,generateDirname(dirnameLength))
        if not os.path.exists(dirName):
            #print(dirName)
            os.mkdir(dirName)
            
            
            #os.chdir(dirName)
            for y in range(numFilesPerDirectory):
                createFiles(dirName,fileSize,totalFiles)
            
        if subdirLevel > 0:
            if subdirCreated < subdirLevel:
                createFolder(dirName,subdirCreated + 1,totalFiles)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calcHowmanyfolders(numFolders, subdirLevel, numFiles, kb):
    foldersOnthislevel = numFolders         #level1
    totalFolders = foldersOnthislevel
    for x in range(1,subdirLevel+1):        #need to add 1 as range does not include last number
        foldersOnthislevel = foldersOnthislevel * numFolders
        totalFolders += foldersOnthislevel

    totalFiles = totalFolders * numFiles
    totalkb = totalFiles * kb / 1000
    print()
    run = input("A total of " + humanreadableNumber(totalFolders) + " folders and " + humanreadableNumber(totalFiles) + " files that will take appr " + humanreadableFilesize(totalkb) + " of diskspace will be created. Ok to continue (Y/N)?")

    if run != 'Y' and run != 'y':
        exit()
    print()
    print()
    return totalFiles   #we need this to show the progress bar

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def progress(count, total, status=''):
    percents = round(100.0 * count / float(total), 1)

    sys.stdout.write('%s%s ...%s\r' % (percents, '%', status))
