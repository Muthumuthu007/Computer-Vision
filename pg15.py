import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("images.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Apply Harris Corner Detection
harris_corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate to mark the corners more clearly
harris_corners = cv2.dilate(harris_corners, None)

# Mark the detected corners in red
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

# Display the result
cv2.imshow("Harris Corner Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
