# Basics

- [x] Loading and Displaying Images
- [x] Getting and Setting Pixels
- [x] Drawing with OpenCV
- [ ] Translation
- [ ] Rotation
- [ ] Resizing
- [ ] Flipping
- [ ] Cropping
- [ ] Image Arithmetic
- [ ] Bitwise Operations
- [ ] Masking
- [ ] Splitting and Merging Channels
  
## Cheatsheet

**Loading and Displaying Images**

```python
# Load the image 
image = cv2.imread("./image_path/image.png")

# Grap the spatial dimensions of image height, width, number of channels
(h, w, c) = image.shape[:3]

# Save the image back to disk
cv2.imwrite("./image_path/image_saved.png")
```

**Getting and Setting Pixels**

```python
# images are simpy NumPy arrays 
# with the origin (0, 0) located at 
# the top-left of the image
(b, g, r) = image[0, 0]

# Acces the pixel location at x = 20 and y = 50 
(b, g, r) = image[20, 50]
```

**Drawing with OpenCV**

```python
# initialize a canvas as 300x300 pixel image with 3 channels
canvas = np.zeros((300, 300, 3), dtype = "uint8")
```

**Translation**

```python
# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image, shape[1], image.shape[0]))

# use the imutils helper function to translate the image 100 pixels down in a single function call
shifted = imutils.translate(image, 0, 100)

```

**Rotation**

```python
# Problematic
rotated = imutils.rotate(image, angle) 

# Loop over the rotation angles again
rotated = imutils.rotate_bound(image, angle)
```

**Resizing**

```python
# Resize the image to be 150 pixels wide
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2. INTER_AREA)
```

- Interpolation methods

```python
methods = [
 ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
 ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
 ("cv2.INTER_AREA", cv2.INTER_AREA),
 ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
 ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

```

- Loop over the interpolation methods

```python
for (name, method) in methods:
    # increase the size of the image by 3x using the current interpolation method
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
```

**Flipping**

```python
# horizontally is 1
flipped = cv2.flip(image, 1)

# vertically is 0
flipped = cv2.flip(image, 1)


# along the both axes is -1
flipped = cv2.flip(image, 1)
```

**Cropping**

```python
# use simple NumPy array slices in startY:endY, startX:endX
face = image[85:250, 85:220]
```

**Image Arithmetic**

```python
# images are NumPy arrays stored as unsigned 8-bit integers (unit8)
# with values in the range [0, 255] when using the add/subtract
# functions in OpenCV, these values will be *clipped* to this range
# even if they fall outside the range [0, 255] after applying the operation

added = cv2.added(np.uint([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
```

**Bitwise Operations**

```python

```

**Masking**

```python

```

**Splitting and Merging Channels**

```python

```

### OpenCV Basics - Assesment

- What is the position of the argument in which radius of the circle is specified in cv2.circle()?

- What are the possible value(s) to be passed as the thickness argument in cv2.rectangle in order to draw a rectangle with solid lines?

- Which of the following can draw a blue rectangle on an image variable, canvas from starting point (10, 20) and ending point (40, 35) with pixel thickness of 2 pixels?

- How can an image be translated right-upwards?

- Which of the following can generate a  translation matrix to shift an image 25 pixels to the right and 50 pixels down?

- If M is the translation matrix, how is the Tx element referenced in M?

- Which of the following perform(s) an image translation of image matrix, canvas with translation matrix, M?

- Which of the following can generate a Rotation Matrix intended to rotate an image with centers, (x, y) by 45 degrees as well as retaining the original dimensions of the image?

- Which of the following function calls could rotate a given image 45 degrees clockwise?

- Which of the following can rotate an image (image matrix, canvas) by 45 degrees without getting the image cropped?

- Which of the following is the aspect ratio of the image h=340 and w=120?

- Which of the following resize(s) an image to width of 100 pixels and retaining aspect ratio given the original image matrix, image?

- Which of the following is the simplest interpolation approach followed in image resizing?
  
- Which of the following interpolation methods performs bilinear interpolation?

- What is the dimension of pixel neighbor which is operated on by interpolation method, cv2.INTER_CUBIC?
  
- What is the dimension of pixel neighbor which is operated on by interpolation method, cv2.INTER_LANCZOS4?
  
- Which of the following interpolation methods provides the highest quality results at a modest computation cost?
  
- What is the flip code for flipping an image only vertically?
  
- Which of the following OpenCV functions is used for executing bitwise XOR among 2 images?
  
- Which of the following merges the R-Channel, G-Channel and B-Channel of an RGB Image to get the RGB Image back in its original form?
  
- What does the following slicing syntax mean? image[90:450, 1:290]

- Which of the following OpenCV functions can perform masking?
  
- What is/are real-life use-case application(s) of image arithmetic?
  
- If the resolution of an image is 120 x 110, calculate the number of pixels present in the image.
  
    Consider the following code snippet:

    ```
    (x, y, z) = image[12, 13] # image is an RGB Image Matrix of dimension (100, 100, 3)
    ```

- Which channel does the pixel value, z point to?
