from helpers import *
from cv2 import destroyAllWindows
import numpy as np


# Change to directory 
process_folder = "04_basic-thresholding"
createFolder(process_folder)

# load the image, display it to our screen, and construct a list of
# bilateral filtering parameters that we are going to explore
image = cv2.imread("images_original/coins02.png")
cv2.imshow("Original", image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# apply Otsu's automatic thresholding which automatically determines
# the best threshold value
(T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))

# visualize only the masked regions in the image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)