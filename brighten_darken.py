import cv2

image = cv2.imread("cat.jpg")

a = 1
b = 0

clicked_plus = False
clicked_minus = False

# press + to initiate brightening process and press a or b to increase the alpha and beta respectively
# press - to initiate darkening process and press a or b to decrease the alpha and beta respectively
# press r to reset to original image
# press esc to end the program

while True:
    new_image = cv2.convertScaleAbs(image, alpha=a, beta=b)
    new_image = cv2.resize(new_image, None, fx=0.2, fy=0.2)
    cv2.imshow("image", new_image)
    key = cv2.waitKey(1)
    if key == ord('r'):
        clicked_plus = False
        clicked_minus = False
        a = 1
        b = 0
    elif key == 27:
        break
    elif key == ord('+'):
        clicked_plus = True
        clicked_minus = False
    elif key == ord('-'):
        clicked_minus = True
        clicked_plus = False
    elif clicked_plus:
        if key == ord('a'):
            a += 0.1
        elif key == ord('b'):
            b += 5
    elif clicked_minus:
        if key == ord('a'):
            a = max(0, a-0.1)
        elif key == ord('b'):
            b -= 5
