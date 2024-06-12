import cv2

'''
sudo apt install v4l-utils
v4l2-ctl --list-devices

sudo apt install ffmpeg
ffplay /dev/video0
'''


# Initialize the webcam
cap = cv2.VideoCapture(3)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()