from matplotlib import pyplot as plt
from helpers import createFolder
import numpy as np
import cv2


# Change to directory 
process_folder = "01_image-histograms"
createFolder(process_folder)


def plot_histogram(image, title, mask=None):
	# split the image into its respective channels, then initialize
	# the tuple of channel names along with our figure for plotting
	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")

	# loop over the image channels
	for (chan, color) in zip(chans, colors):
		# create a histogram for the current channel and plot it
		hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
		plt.plot(hist, color=color)
		plt.xlim([0, 256])

# load the beach image and plot a histogram for it
image = cv2.imread("images_original/lane0.jpeg")
cv2.waitKey(0)
plot_histogram(image, "Histogram for Original Image")
cv2.imshow("Original", image)


# construct a mask for our image; our mask will be *black* for regions
# we want to *ignore* and *white* for regions we want to *examine*
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (60, 290), (210, 390), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

# display the masked region
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the Mask", masked)
cv2.waitKey(0)

# compute a histogram for our image, but we'll only include pixels in
# the masked region
plot_histogram(image, "Histogram for Masked Image", mask=mask)
cv2.waitKey(0)

# show our plots
plt.show()