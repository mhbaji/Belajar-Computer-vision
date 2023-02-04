import cv2
import mediapipe
import time 
solusi_face_detection = mediapipe.solutions.face_detection
face_detection = solusi_face_detection.FaceDetection()

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
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result_detection = face_detection.process(image)
    if not result_detection.detections:
        continue
    
    height_image, width_image = image.shape[:-1]
    for detection in result_detection.detections:
        print(detection.location_data.relative_bounding_box)
        x_min = int(detection.location_data.relative_bounding_box.xmin*width_image)
        y_min = int(detection.location_data.relative_bounding_box.ymin*height_image)
        width_face = int(detection.location_data.relative_bounding_box.width*width_image)
        height_face = int(detection.location_data.relative_bounding_box.height*height_image)
        cv2.rectangle(image, (x_min, y_min), (x_min+width_face, y_min+height_face), (0, 0, 255), 2)

    print("waktu", time.time()-_time_mulai)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (540, 960))
    cv2.imshow("image", image)
    _key = cv2.waitKey(1)
    if _key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()