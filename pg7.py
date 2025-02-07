import cv2

# Open the video capture
cap = cv2.VideoCapture('video.mp4')  # Replace with 0 to capture from the camera

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break
        
        # Display the video at normal speed
        cv2.imshow('Normal Speed', frame)

        # For slow motion (increase wait time between frames)
        cv2.imshow('Slow Motion', frame)
        cv2.waitKey(100)  # Slow motion (100 ms between frames)

        # For fast motion (decrease wait time between frames)
        cv2.imshow('Fast Motion', frame)
        cv2.waitKey(10)  # Fast motion (10 ms between frames)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
