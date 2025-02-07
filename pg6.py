import cv2
import numpy as np

# Read the image
image = cv2.imread('images.jpeg')

# Check if the image was loaded properly
if image is None:
    print("Error: Image not loaded.")
else:
    # Define the kernel for the erosion operation
    kernel = np.ones((5, 5), np.uint8)
    
    # Apply the erosion function
    eroded_image = cv2.erode(image, kernel, iterations=1)
    
    # Display the original and eroded images
    cv2.imshow('Original Image', image)
    cv2.imshow('Eroded Image', eroded_image)
    
    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
