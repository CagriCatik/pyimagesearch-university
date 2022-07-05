from helpers import *
from cv2 import destroyAllWindows
import numpy as np


# Change to directory 
process_folder = "02_smoothing-and-blurring"
createFolder(process_folder)

# load the image, display it to our screen, and construct a list of
# bilateral filtering parameters that we are going to explore
image = cv2.imread("images_original/lena.png")

diameter, sigmaColor, sigmaSpace= 0, 0, 0

blurred0 = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
cv2.imshow(title, blurred0)
cv2.waitKey(0)

diameter, sigmaColor, sigmaSpace= 11, 21, 7

blurred1 = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
cv2.imshow(title, blurred1)
cv2.waitKey(0)

diameter, sigmaColor, sigmaSpace= 11, 41, 21

blurred2 = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
cv2.imshow(title, blurred2)
cv2.waitKey(0)


diameter, sigmaColor, sigmaSpace= 11, 61, 39

blurred3  = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
cv2.imshow(title, blurred3)
cv2.waitKey(0)

compare = get_concat_h(blurred0, blurred1, blurred2, blurred3)
cv2.imwrite("./images_solution/horizontal.jpg", compare)
cv2.imshow("Compare images", compare)
cv2.waitKey(0)
destroyAllWindows()

# Loop over 
'''
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering to the image using the current set of
	# parameters
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)

	# show the output image and associated parameters
	title = "Blurred d={}, sc={}, ss={}".format(
		diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)

'''