import cv2
import numpy as np

# Read the image
image = cv2.imread('images.jpeg')

if image is None:
    print("Error: Image not loaded.")
else:
    # Define the kernel for the dilation operation
    kernel = np.ones((5, 5), np.uint8)

    # Apply the dilation function
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display the original and dilated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Dilated Image', dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
