# sobel and find edges of imageS
import cv2 as cv
import numpy as np

# 1. Load the image
img = cv.imread(r'C:\\Users\\Admin\\Pictures\\plate.jpg')

# Check whether the image loaded successfully
if img is None:
    print("Error: Image not found. Check the file path.")
    raise SystemExit

# 2. Convert the color image to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 3. Apply the Sobel operator in the X direction
# CV_32F stores positive and negative gradient values.
# dx=1, dy=0 calculates the horizontal intensity derivative.
sobelx = cv.Sobel(grey, cv.CV_32F, 1, 0, ksize=3)

# 4. Find minimum and maximum gradient values
minVal = np.min(sobelx)
maxVal = np.max(sobelx)

print("Minimum Sobel value:", minVal)
print("Maximum Sobel value:", maxVal)

# 5. Normalize the result to display it as an 8-bit image
if maxVal > minVal:
    draw = cv.normalize(
        sobelx, None, 0, 255, cv.NORM_MINMAX
    ).astype(np.uint8)
else:
    draw = np.zeros_like(grey)

# 6. Display the images
cv.imshow("Original Image", img)
cv.imshow("Grayscale Image", grey)
cv.imshow("Sobel X - Edge Result", draw)

# 7. Wait until a key is pressed, then close windows
cv.waitKey(0)
cv.destroyAllWindows()
