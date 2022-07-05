import numpy as np
import imutils, cv2
from helpers import createFolder

# Change to directory 
process_folder = "05_opencv-rotate"
createFolder(process_folder)

# load the image and display it to our screen
image = cv2.imread("images_original/pill_01.png")

cv2.imshow("Original", image)
cv2.waitKey(0)

# convert the original image to grayscale
grayConverted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./images_solution/grayscale.jpg", grayConverted)
cv2.imshow("Grayscale", grayConverted)
cv2.waitKey(0)

# blur the converted image
bluredImage = cv2.GaussianBlur(grayConverted, (3, 3), 0)
cv2.imwrite("./images_solution/blured.jpg", bluredImage)
cv2.imshow("Gaussian blur", bluredImage)
cv2.waitKey(0)

# canny edge detection to reveal the outline of the pill
edged = cv2.Canny(bluredImage, 20, 100)
cv2.imwrite("./images_solution/canny.jpg", edged)
cv2.imshow("Canny edge", edged)
cv2.waitKey(0)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# ensure at least one contour was found
if len(cnts) > 0:
	# grab the largest contour, then draw a mask for the pill
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(bluredImage.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)

	# compute its bounding box of pill, then extract the ROI,
	# and apply the mask
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)

	# loop over the rotation angles
	for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate(imageROI, angle)
		cv2.imshow("Rotated (Problematic)", rotated)
		cv2.imwrite("./images_solution/rotating_image_problematic.jpg", image)
		cv2.waitKey(0)

	# loop over the rotation angles again, this time ensure the
	# entire pill is still within the ROI after rotation
	for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate_bound(imageROI, angle)
		cv2.imshow("Rotated (Correct)", rotated)
		cv2.imwrite("./images_solution/rotating_image.jpg", image)
		cv2.waitKey(0)