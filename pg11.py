import cv2

# Read the image
image = cv2.imread('images.jpeg')

if image is None:
    print("Error: Image not loaded.")
else:
    # Rotate the image 180 degrees clockwise (two 90-degree rotations)
    rotated_image_180 = cv2.rotate(image, cv2.ROTATE_180)

    # Display the rotated image
    cv2.imshow('180 Degree Rotated Image', rotated_image_180)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
