from helpers import *
from cv2 import destroyAllWindows
import numpy as np


# Change to directory 
process_folder = "02_smoothing-and-blurring"
createFolder(process_folder)

# load the image, display it to our screen, and construct a list of
# bilateral filtering parameters that we are going to explore
image = cv2.imread("images_original/lena.png")

kernelSizes = [(3, 3), (9, 9), (15, 15)]

# loop over the kernel sizes
for (kX, kY) in kernelSizes:
	# apply an "average" blur to the image using the current kernel
	# size
	blurred = cv2.blur(image, (kX, kY))
	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernel sizes again
for (kX, kY) in kernelSizes:
	# apply a "Gaussian" blur to the image
	blurred = cv2.GaussianBlur(image, (kX, kY), 0)
	cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernel sizes a final time
for k in (3, 9, 15):
	# apply a "median" blur to the image
	blurred = cv2.medianBlur(image, k)
	cv2.imshow("Median {}".format(k), blurred)
	cv2.waitKey(0)