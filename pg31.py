import cv2
import numpy as np

def segment_image(image_path, threshold_value=127):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply thresholding
    _, segmented = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
segment_image("images.jpeg", 127)
