import cv2
import numpy as np

# Load the image
image = cv2.imread("images.jpeg")

# Get image dimensions
h, w = image.shape[:2]

# Define four points for Perspective Transformation
src_pts = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])
dst_pts = np.float32([[0, 0], [w-1, 50], [50, h-1], [w-50, h-50]])

# Compute the Perspective Transformation matrix
persp_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)

# Apply the transformation
persp_img = cv2.warpPerspective(image, persp_matrix, (w, h))

# Display the result
cv2.imshow("Perspective Transformation", persp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
