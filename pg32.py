import cv2
import numpy as np

def create_colored_corners(image_size):
    img = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255  # White image
    box_size = image_size // 10  # 1/10th of image size

    # Draw four boxes in the corners
    img[:box_size, :box_size] = (0, 0, 0)  # Black (Top Left)
    img[:box_size, -box_size:] = (255, 0, 0)  # Blue (Top Right)
    img[-box_size:, :box_size] = (0, 255, 0)  # Green (Bottom Left)
    img[-box_size:, -box_size:] = (0, 0, 255)  # Red (Bottom Right)

    # Display image
    cv2.imshow("Colored Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
create_colored_corners(500)
