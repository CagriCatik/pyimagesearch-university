
import numpy as np
import imutils, cv2
from helpers import createFolder

# Change to directory 
process_folder = "12_split-merge"
createFolder(process_folder)


# load the image and display it to our screen
image = cv2.imread("images_original/opencv_logo.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# load the input image and grab each channel -- note how OpenCV
# represents images as NumPy arrays with channels in Blue, Green,
# Red ordering rather than Red, Green Blue

(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imwrite("./images_solution/red.jpg", image)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.imwrite("./images_solution/green.jpg", image)
cv2.waitKey(0)

cv2.imshow("Blue", B)
cv2.imwrite("./images_solution/blue.jpg", image)
cv2.waitKey(0)

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.imwrite("./images_solution/merged.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)