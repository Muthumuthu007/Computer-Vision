import cv2
import numpy as np

def create_circle(image_size):
    img = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255  # White image

    # Draw a circle (radius is 1/4 of the image size)
    center = (image_size // 2, image_size // 2)
    radius = image_size // 4
    cv2.circle(img, center, radius, (0, 255, 0), 3)

    # Display image
    cv2.imshow("Circle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
create_circle(500)
