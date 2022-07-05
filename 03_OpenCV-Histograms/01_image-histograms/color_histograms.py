import imutils
import cv2
from matplotlib import pyplot as plt
from helpers import createFolder

# Change to directory 
process_folder = "01_image-histograms"
createFolder(process_folder)

# load the image and display it to our screen
image = cv2.imread("images_original/lane1.jpeg")
cv2.imshow("Original", image)
#cv2.imwrite("./images_solution/original.jpg", image)
cv2.waitKey(0)

# split the image into its respective channels, then initialize the
# tuple of channel names along with our figure for plotting
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.savefig('./plots_solution/flattened.png')

# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and plot it
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])

# create a new figure and then plot a 2D color histogram for the green and blue channels
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
 

# plot a 2D color histogram for the green and red channels
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)
 

# plot a 2D color histogram for blue and red channels
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.savefig('./plots_solution/2d_color_hist_B_R.png')

# finally, let's examine the dimensionality of one of the 2D histograms
print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

# our 2D histogram could only take into account 2 out of the 3
# channels in the image so now let's build a 3D color histogram
# (utilizing all channels) with 8 bins in each direction -- we
# can't plot the 3D histogram, but the theory is exactly like
# that of a 2D histogram, so we'll just show the shape of the
# histogram

hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))

# display the original input image
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))
plt.savefig('./plots_solution/original_image.png')

# show our plots
plt.show()