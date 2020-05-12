import random
import string
import os
import sys #for progress bar

from localFunctions import generateRandomness
from localFunctions import generateFilename
from localFunctions import generateDirname
from localFunctions import humanreadableNumber
from localFunctions import humanreadableFilesize
from localFunctions import createFiles
from localFunctions import createFolder
from localFunctions import calcHowmanyfolders
from localFunctions import progress

i = 0

system('cls' if os.name == 'nt' else 'clear')

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
