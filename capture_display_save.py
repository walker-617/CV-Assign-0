import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Unable to open camera.")
else:
    while True:
        result, image = cam.read()

        if not result:
            print("Unable to capture image.")
            break

        cv2.imshow("Live", image)

        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.imwrite("captured_image.jpg", image)
            cam.release()
            cv2.destroyAllWindows()
            cv2.imshow("Captured image", image)
            cv2.waitKey(0)
            break

        elif key == 27:
            break
