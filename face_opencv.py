import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# path_video = "video.mp4"
path_video = 0
cam = cv2.VideoCapture(path_video)
if not cam.isOpened():
    raise("No Camera")

while True:
    ret, image = cam.read()
    if not ret:
        break
    
    _time_mulai = time.time()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    print('waktu', time.time()-_time_mulai)
    image = cv2.resize(image, (540, 960))
    cv2.imshow("image", image)
    _key = cv2.waitKey(1)
    if _key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()