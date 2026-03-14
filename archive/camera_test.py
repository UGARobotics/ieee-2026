import cv2

cap = cv2.VideoCapture(0)   # 0 = /dev/video0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if ret:
        cv2.imwrite("frame.jpg", frame)
        break
    
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:   # ESC
        break

cap.release()
cv2.destroyAllWindows()
