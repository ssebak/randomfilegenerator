import random
import string
import os


from localFunctions import generateRandomness
from localFunctions import generateFilename
from localFunctions import generateDirname
from localFunctions import calcHowmanyfolders
from localFunctions import progress
from localFunctions import getNumericValue

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

    progress(i, totalFiles, status='Creating files ....')
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


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

subdirLevel_default = 0
numDirectories_default = 1


subdirLevel = getNumericValue("How many subfolder levels should be created in addition to the top folder (" + str(subdirLevel_default) + "): ")
numDirectories = getNumericValue("How many folders should be created in each subfolder (" + str(numDirectories_default) + "): ")
numFilesPerDirectory = getNumericValue("How many files should be created in each folder: ")
fileSize = getNumericValue("How large (in KB) should each file be: ", 'float')
fileSize *= 1024

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