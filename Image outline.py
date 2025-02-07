import cv2

image = cv2.imread('images.jpeg')  

if image is None:
    print("Error: Could not read the image.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_image, 100, 200)

    cv2.imwrite('edge_image.jpg', edges)

    cv2.imshow('Original Image', image)
    cv2.imshow('Edge-detected Image', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
