import cv2
from ultralytics import YOLO
import supervision as sv

# 获取摄像头
cap = cv2.VideoCapture(0)

# 定义模型
model = YOLO('yolov8l.pt')

box_annotator = sv.BoxAnnotator(
    thickness=2,
    text_thickness=2,
    text_scale=1
)

# results = model.train(epochs=5)

# 实时录像
while 1:
    ret, frame = cap.read()
    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)
    # print(detections)

    labels = [
        f"{model.model.names[detections.class_id[0]]} {detections.confidence[0]:0.2f}"
    ]

    frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)

    cv2.imshow("name", frame)  # cv2.flip(results, 1))
    if cv2.waitKey(1) == ord('q'):
        break
    # 按下 s 保存
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
