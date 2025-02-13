from ultralytics import YOLO
import os


model = YOLO('yolov8n.pt')
results = model.train(
    data="dt.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    name='det_janelas',
    project="./runs",
    degrees=20,
    flipud=0.5,
    fliplr=0.5,
    scale=0.5,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    mosaic=1.0,
    mixup=0.2
)