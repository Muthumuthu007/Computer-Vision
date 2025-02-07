import cv2

# Read the image
image = cv2.imread('images.jpeg')

if image is None:
    print("Error: Image not loaded.")
else:
    # Rotate the image 270 degrees clockwise (equivalent to 90-degree counterclockwise)
    rotated_image_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the rotated image
    cv2.imshow('270 Degree Rotated Image', rotated_image_270)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
