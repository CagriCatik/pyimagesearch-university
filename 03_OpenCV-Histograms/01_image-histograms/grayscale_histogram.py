from matplotlib import pyplot as plt
from helpers import createFolder
import cv2

# Change to directory 
process_folder = "01_image-histograms"
createFolder(process_folder)

# load the input image and convert it to grayscale
image = cv2.imread("images_original/lane0.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute a grayscale histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# matplotlib expects RGB images so convert and then display the image
# with matplotlib
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

# normalize the histogram
hist /= hist.sum()

# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()