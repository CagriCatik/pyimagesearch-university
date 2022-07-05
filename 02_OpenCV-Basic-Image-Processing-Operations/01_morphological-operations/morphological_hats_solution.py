from helpers import *
from cv2 import destroyAllWindows
import numpy as np


# Change to directory 
process_folder = "01_morphological-operations"
createFolder(process_folder)

# load the image and display it to our screen
image = cv2.imread("images_original/car.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

 # load the image and convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light background
rectangular_kernel = (14,6)
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, rectangular_kernel)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a tophat (also called a "whitehat") operation will
# enable us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
 
horizontal = get_concat_h(tophat, blackhat) 
cv2.imshow("tophat vs blackhat", horizontal)
cv2.imwrite("./images_solution/horizontal.jpg", horizontal)
cv2.waitKey(0) 
destroyAllWindows()
 