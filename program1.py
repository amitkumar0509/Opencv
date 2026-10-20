
# ============================================================
# TOPIC 1: IMPORTING OPENCV AND CHECKING ITS VERSION
# ============================================================

import cv2
import numpy as np

# cv2 is the OpenCV library used for image processing.
# numpy is used for working with arrays and lookup tables.

print("OpenCV version:", cv2.__version__)

# __version__ displays the installed version of OpenCV.


# ============================================================
# TOPIC 2: READING AN IMAGE AND DISPLAYING ITS MATRIX
# ============================================================

# imread() loads an image from the specified file path.
# IMREAD_COLOR loads the image in color (BGR format).
# The image is stored as a NumPy array.

img = cv2.imread(
    r"C:\Users\Admin\Pictures\plate.jpg"
)

# Check whether the image was loaded successfully.
# If the path is incorrect, img will be None.

if img is None:
    print("Error: Image not found. Check the file path.")

else:
    # Print the image's pixel values.
    # Each color pixel contains Blue, Green and Red values.
    print("Image matrix:")
    print(img)

    # Display the original image in a window.
    cv2.imshow("Original Image", img)

    # Wait until a key is pressed.
    # 0 means wait indefinitely.
    cv2.waitKey(0)

    # Close all OpenCV image windows.
    cv2.destroyAllWindows()


# ============================================================
# TOPIC 3: SCANNING AN IMAGE PIXEL BY PIXEL
# ============================================================

# Convert the image to grayscale.
# Each pixel now has one intensity value from 0 to 255.
# 0 = black, 255 = white.

gray = cv2.imread(
    r"C:\Users\Admin\Pictures\plate.jpg",
    cv2.IMREAD_GRAYSCALE
)

if gray is not None:

    # Get image dimensions.
    # height = number of rows
    # width  = number of columns
    height, width = gray.shape

    print("Image height:", height)
    print("Image width:", width)

    # Scan every pixel row by row.
    # y represents the row index.
    # x represents the column index.
    for y in range(height):
        for x in range(width):

            # Read the intensity value at row y, column x.
            pixel = gray[y, x]

            # Print the pixel's intensity.
            # Note: Printing every pixel can produce a huge output.
            # Uncomment the next line if you want to inspect them.
            # print(f"Pixel ({y}, {x}) = {pixel}")

    print("Image scanning completed.")

else:
    print("Error: Grayscale image not found.")


# ============================================================
# TOPIC 4: LOOKUP TABLE (LUT) FOR IMAGE INVERSION
# ============================================================

# A lookup table stores an output value for each possible input.
# For an 8-bit grayscale image, there are 256 possible values:
# 0, 1, 2, ..., 255.
#
# Image inversion formula:
# output pixel = 255 - input pixel
#
# Examples:
# input 0   -> output 255 (black becomes white)
# input 100 -> output 155
# input 255 -> output 0   (white becomes black)

if gray is not None:

    # Create a lookup table containing 256 entries.
    # np.uint8 stores values as unsigned 8-bit integers (0-255).
    lut = np.array(
        [255 - i for i in range(256)],
        dtype=np.uint8
    )

    # Apply the lookup table to every pixel.
    # OpenCV performs this transformation efficiently.
    inverted = cv2.LUT(gray, lut)

    # Display the original grayscale image.
    cv2.imshow("Original Grayscale Image", gray)

    # Display the inverted image.
    cv2.imshow("Inverted Image", inverted)

    # Wait for a key press before closing the windows.
    cv2.waitKey(0)

    cv2.destroyAllWindows()


# ============================================================
# TOPIC 5: TIME MEASUREMENT IN OPENCV
# ============================================================

# Time measurement helps determine how long an operation takes.
# Here, we measure the execution time of Gaussian blur.
#
# getTickCount() returns a high-resolution counter value.
# getTickFrequency() returns the counter ticks per second.

if gray is not None:

    # Record the counter value before processing.
    start = cv2.getTickCount()

    # Apply Gaussian blur to reduce image noise.
    # (5, 5) specifies the kernel width and height.
    # 0 lets OpenCV calculate sigma from the kernel size.
    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Record the counter value after processing.
    end = cv2.getTickCount()

    # Calculate elapsed time in seconds.
    # Formula:
    # time = (end counter - start counter) / tick frequency
    elapsed = (
        end - start
    ) / cv2.getTickFrequency()

    print("Gaussian blur time:", elapsed, "seconds")

    # Display the blurred result.
    cv2.imshow("Gaussian Blur", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Cannot process image because it was not loaded.")
