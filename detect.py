import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    cv2.imshow("name", cv2.flip(frame, 1))
    if cv2.waitKey(1) == ord('q'):
        break
    # 按下 s 保存
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
