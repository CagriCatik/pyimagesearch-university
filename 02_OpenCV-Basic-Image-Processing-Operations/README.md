# OpenCV - Basic Image Processing Operations

- [x] Morphological Operations
- [x] Smoothing and Blurring
- [x] Color spaces
- [x] Basic thresholding
- [ ] Adaptive thresholding
- [ ] Kernels
- [ ] Image gradients
- [ ] Edge detection
- [ ] Automatic edge detection

## Cheatsheet

### Morphological Operations

#### **Erosion**
  
```python
# Erosion operation for 1 iteration
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eroded = cv2.erode(gray, None, iterations=1)
```

#### **Dilate**
  
```python
# Erosion operation for 1 iteration
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dilated = cv2.dilate(gray, None, iterations=1)
```

#### **Blackhat operation**

```python
# first convert the image  to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light background
rectangular_kernel = (14,6)
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, rectangular_kernel)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
```

#### **Tophat Operation**

```python
# Tophat operation will enable us to find light regions on a dark background
rectangular_kernel = (14,6)
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, rectangular_kernel)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

```

#### **Opening**
  
```python
# Opening operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
```

#### **Closing**
  
```python
# Closing operation for different kernelSizes
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
```

#### **Gradient Operation**
  
```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```

### Smoothing and Blurring

#### **Bilateral Filter**

```python
# bilateral filtering parameters
diameter, sigmaColor, sigmaSpace = 11, 21, 7
blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)

```

#### **Blurring**

```python
# bilateral filtering parameters
kX, kY = 3, 3

#apply an "average" blur to the image using the current kernel
blurred = cv2.blur(image, (kX, kY))

# apply a "Gaussian" blur to the image
blurred = cv2.GaussianBlur(image, (kX, kY), 0)

# apply a "median" blur to the image
blurred = cv2.medianBlur(image, k)
```

### Color Spaces

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```

### Thresholding

#### **Simple Thresholding**

```python
# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be *black, otherwise it is *white*
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
 
# using normal thresholding (rather than inverse thresholding)
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
```

#### **OTSU Thresholding**

```python
# apply Otsu's automatic thresholding which automatically determines
# the best threshold value
# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# apply Otsu's automatic thresholding which automatically determines the best threshold value
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
 
```


### Thresholding

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```

### Adaptive Thresholding

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```

### Convolutions

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```


### Image Gradients

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```

### Canny Edge Detector

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```


### Auto Canny

#### **Bilateral**

```python
# Gradient operation for different kernelSizes
kernelSizes = [(3, 3), (5, 5), (7, 7)]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```