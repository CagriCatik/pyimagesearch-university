
import numpy as np
import imutils, cv2
from helpers import createFolder

# Change to directory 
process_folder = "04_opencv-translate"
createFolder(process_folder)


# load the image and display it to our screen
image = cv2.imread("images_original/opencv_logo.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.imwrite("./images_solution/shifted-down-right.jpg", image)
cv2.waitKey(0)

# now, let's shift the image 50 pixels to the left and 90 pixels
# up by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.imwrite("./images_solution/shifted-up-left.jpg", image)
cv2.waitKey(0)

# use the imutils helper function to translate the image 100 pixels
# down in a single function call
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.imwrite("./images_solution/shifted-down.jpg", shifted)
cv2.waitKey(0)