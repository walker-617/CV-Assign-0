import cv2

video = cv2.VideoCapture(0)

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter(
    'video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)

text = ""
click = False

while(True):
    ret, image = video.read()
    if click:
        result.write(image)
    show_image = cv2.putText(
        image, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow('Frame', show_image)
    key = cv2.waitKey(1)
    if key == 32:
        click = True
        text = "Recording..."
    elif key == ord('s'):
        break

video.release()
result.release()

cv2.destroyAllWindows()

cap = cv2.VideoCapture('video.mp4')
while cap.isOpened():
    ret, image = cap.read()
    if ret == True:
        cv2.imshow('Recorded video', image)
        key = cv2.waitKey(25)
        if key == ord('q') or key == 27:
            break
    else:
        break

cap.release()
