import cv2
import numpy as np

def remove_background(image_path, lower_bound, upper_bound):
    image = cv2.imread(image_path)

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create mask based on color range
    mask = cv2.inRange(hsv, np.array(lower_bound), np.array(upper_bound))

    # Apply mask to remove background
    result = cv2.bitwise_and(image, image, mask=~mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("Background Removed", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage (removing green background)
remove_background("images.jpeg", [35, 40, 40], [85, 255, 255])
