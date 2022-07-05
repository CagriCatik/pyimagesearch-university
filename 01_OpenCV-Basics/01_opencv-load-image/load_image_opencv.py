import cv2, os, shutil
 
os.chdir("01_opencv-load-image")

# Check existence of a folder and then remove it

path = "./images_solution/"

if os.path.exists(path) and os.path.isdir(path):
    shutil.rmtree(path)

# Create a folder for solutions  

os.mkdir(path)

# load the image from disk via "cv2.imread" and then grab the spatial
# dimensions, including width, height, and number of channels

image_path = "./images/OpenCV.png"
image = cv2.imread(image_path)
(h, w, c) = image.shape[:3]

# display the image width, height, 
# and number of channels to our terminal

print("width	: {} pixels	".format(w))
print("height	: {} pixels	".format(h))
print("channels	: {}		".format(c))

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk 
# (OpenCV handles converting image
# filetypes automatically)
cv2.imwrite("./images_solution/OpenCV_saved.jpg", image)