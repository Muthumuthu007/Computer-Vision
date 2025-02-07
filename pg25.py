import cv2

# Load the pre-trained Haar Cascade model for watches (ensure you have the XML file)
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")  # Replace with the correct path

# Load the input image
image = cv2.imread("watch_image.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches in the image
watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw bounding boxes around detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Display the result
cv2.imshow("Watch Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
