import numpy as np
import imutils, cv2
from helpers import createFolder

# Change to directory 
process_folder = "05_opencv-rotate"
createFolder(process_folder)

# load the image and display it to our screen
image = cv2.imread("images_original/pill_01.png")

# loop over the rotation angles
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate(image, angle)
	cv2.imshow("Rotated (Problematic)", rotated)
	cv2.waitKey(0)

# loop over the rotation angles again
# this time ensuring no part of the image is cut off
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.waitKey(0)