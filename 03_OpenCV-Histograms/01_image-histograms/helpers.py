# import the necessary packages
import os, shutil

def createFolder(process_folder):

    # Change to directory 
    os.chdir(process_folder)

    # Check existence of a folder and then remove it
    path_image = "./images_solution"
    path_plot = "./plots_solution"

    if os.path.exists(path_image and path_plot) and os.path.isdir(path_image and path_plot):
        shutil.rmtree(path_image and path_plot)


    print("Existence check or remove the existing solution folder")

    # Create a folder for solutions  
    os.mkdir(path_image and path_plot)
