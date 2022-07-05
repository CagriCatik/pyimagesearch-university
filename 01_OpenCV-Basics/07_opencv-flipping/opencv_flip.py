import cv2
from helpers import createFolder

# Change to directory 
process_folder = "07_opencv-flipping"
createFolder(process_folder)

# load the image and display it to our screen
image = cv2.imread("images_original/opencv_logo.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# flip the image horizontally
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.imwrite("./images_solution/horizontally-flipped.jpg", flipped)
cv2.waitKey(0)

# flip the image vertically
flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", flipped)
cv2.imwrite("./images_solution/vertically-flipped.jpg", flipped)
cv2.waitKey(0)

# flip the image along both axes
flipped = cv2.flip(image, -1)
print("[INFO] flipping image horizontally and vertically...")
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.imwrite("./images_solution/horizontally-vertically-flipped.jpg", flipped)
cv2.waitKey(0)