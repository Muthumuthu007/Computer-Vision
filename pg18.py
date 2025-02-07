import cv2

# Load the image
image = cv2.imread("images.jpeg")

# Define ROI coordinates (x, y, width, height)
x, y, w, h = 100, 100, 200, 200
roi = image[y:y+h, x:x+w]  # Crop the selected region

# Define paste position
x_paste, y_paste = 300, 300
image[y_paste:y_paste+h, x_paste:x_paste+w] = roi  # Paste cropped region

# Display cropped and modified image
cv2.imshow("Cropped Region", roi)
cv2.imshow("Image with Pasted Region", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
