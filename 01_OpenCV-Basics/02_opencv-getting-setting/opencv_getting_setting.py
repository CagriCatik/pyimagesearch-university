# import the necessary packages
import cv2
from helpers import createFolder

# Change to directory 
solution_folder = "02_opencv-getting-setting"
createFolder(solution_folder)

# Load the image from disk via "cv2.imread"
image_path = "./images_original/OpenCV.png"
image = cv2.imread(image_path)

print("image loadad from folder")
image_name = "Original"


# Grab the spatial dimensions, including width, height, and number of channels
(h, w, c) = image.shape[:3]

print("height   :", format(h))
print("width    :", format(w))
print("channels :", format(c))

# Show the image
cv2.imshow(image_name, image)

# images are simply NumPy arrays with the origin (0, 0) located at the top-left of the image
(b, g, r) = image[0, 0]
print("Pixel at origin      = RED: {}, GREEN: {}, BLUE: {}".format(r, g, b))

# Check if the pixel white green blue
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

# Access the pixel located at x=50, y=20
x_cor, y_cor = 100, 200
(b, g, r) = image[y_cor, x_cor]
print("Pixel at (100, 200)  = RED: {}, GREEN: {}, BLUE: {}".format(r, g, b))

if (r, g, b) == WHITE: 
    print("pixel is white")
elif (r,g,b) == BLUE:
    print("pixel is blue")
elif (r,g,b) == GREEN:
    print("pixel is green")

# Save the image back to disk (OpenCV handles converting image filetypes automatically)
image_name = "original"
cv2.imwrite("./images_solution/OpenCV_"+ str(image_name) +".jpg", image)

# TODO update the pixel at (50, 20) and set it to red


# compute the center of the image, which is simply the width and height divided by two


# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image

# save the image back to disk 
# (OpenCV handles converting image filetypes automatically)


# in a similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our
# screen


# set the top-left corner of the original image to be green


# Show our updated image
cv2.waitKey(0)