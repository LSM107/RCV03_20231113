# !/usr/bin/env python3

import sys
import cv2

window_title = "USB Camera"

def show_camera():
    # ASSIGN CAMERA ADDRESS HERE
    camera_id = 0
    # For webcams, we use V4L2
    video_capture = cv2.VideoCapture(camera_id)

    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE )
            while True:
                ret_val, frame = video_capture.read()

                # Convert the image to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
                # Apply Gaussian blur
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
                # Apply Canny edge detection
                edges = cv2.Canny(blurred, 50, 150)

                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    # Show the processed image instead of the original frame
                    cv2.imshow(window_title , edges)
                    
                else:
                    break

                keyCode = cv2.waitKey(10) & 0xFF
                
                if keyCode == 27 or keyCode == ord('q'):
                    break

        finally:
            video_capture.release()
            cv2.destroyAllWindows()
            
    else:
        print("Unable to open camera")


if __name__ == "__main__":

    show_camera()
