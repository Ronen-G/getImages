#! python3
# Finds image files in a directory and copies them to a single folder

import os, sys, shutil

def fromAddress(folder):
    # Locate and validate directory to copy from.

    if(folder == os.path.exists(folder)):   # make sure destination exsists
        if(folder == os.path.isdir(folder)):    # make sure destination is a directory
            if(folder == os.path.abspath(folder)):    # make sure directory is absolute
                return(folder)
            else:
                print("Directory is not absolute!")
        else:
            print("Destination is not a directory!")
    else:
        print("No such directory.")
    
def toAddress(folder):
    # Locate or create directory to copy to.
    
    # Check if directory exsists - if not, then create it
    if(folder == os.path.exists(folder)):   # make sure destination exsists
        if(folder == os.path.isdir(folder)): # make sure destination is a directory
            if(folder == os.path.abspath(folder)):    # make sure directory is absolute
                return(folder)
            else:
                print("Directory is not absolute!")
        else:
            print("Destination is not a directory!")
    else:
        # Create new folder
        print('\nCreating %s...' % (folder))
        newFolder = os.mkdir(folder)
    return(newFolder)

def walkAndCopy(fromFolder, toFolder):
    # Walks through given directory tree and copies images to given destination
    # looks for .jpg, .bmp, .png, .tiff
    for foldername, subfolders, filename in os.walk(fromFolder):
        print('Adding images in %s...' % (toFolder))
        print('\nCurrent subfolder: %s...' % (subfolders))
        print('\nCurrent file: %s...' % (filename))
        # Copy all the image files in this folder to the new folder.
        for filename in filenames:
            shutil.copy(filename, toFolder)

    print('\nDone.')

fromA = fromAddress(str(input("Copy From? ")))
toA = toAddress(str(input("Copy to? ")))
walkAndCopy(fromA, toA)
