import cv2
import numpy as np

def create_rectangle(image_size):
    img = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255  # White image

    # Draw a rectangle (thickness 3)
    cv2.rectangle(img, (100, 100), (image_size - 100, image_size - 100), (0, 0, 255), 3)

    # Display image
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
create_rectangle(500)
