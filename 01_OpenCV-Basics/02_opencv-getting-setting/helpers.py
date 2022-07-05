# import the necessary packages
import os, shutil

def createFolder(process_folder):

    # Change to directory 
    os.chdir(process_folder)

    # Check existence of a folder and then remove it
    path = "./images_solution"

    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

    print("Existence check or remove the existing solution folder")

    # Create a folder for solutions  
    os.mkdir(path)
