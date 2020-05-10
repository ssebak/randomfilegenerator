import random
import string
import os
import sys #for progress bar

from localFunctions import generateRandomness
from localFunctions import generateFilename
from localFunctions import generateDirname
from localFunctions import humanreadableNumber
from localFunctions import humanreadableFilesize

i = 0

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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


os.system('cls')

subdirLevel_default = 0
numDirectories_default = 1

subdirLevel = input("How many subfolder levels should be created in addition to the top folder (" + str(subdirLevel_default) + "): ")
if not subdirLevel.strip():
    #empty string, use default value
    subdirLevel = subdirLevel_default
else:
    subdirLevel = int(subdirLevel)

numDirectories = input("How many folders should be created in each subfolder (" + str(numDirectories_default) + "): ")
if not numDirectories.strip():
    #empty string, use default value
    numDirectories = numDirectories_default
else:
    numDirectories = int(numDirectories)

numFilesPerDirectory = int(input("How many files should be created in each folder: "))
fileSize = int(input("How large (in KB) should each file be: "))
fileSize *= 10

dirStart = str(input("Enter path for creating folders and files (" + os.getcwd() + "): "))
if not dirStart:
    dirStart = os.getcwd()
elif not os.path.isdir(dirStart):
    print("\nDirectory " + dirStart + " does not exist.")
    exit()

filenameLength = 8
filenameExtension = "txt"
dirnameLength = 8
subdirCreated = 0
#dirStart = "c:/projects/randomfiles/files"

totalFiles = calcHowmanyfolders(numDirectories,subdirLevel,numFilesPerDirectory,fileSize)

os.chdir(dirStart)

createFolder(dirStart,0,totalFiles)

print("Done creating directories",end = '')
print('.')