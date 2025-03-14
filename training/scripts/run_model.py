from ultralytics import YOLO

model = YOLO("runs/det_all3/weights/best.pt")

results = model.predict("dataset/images/test/7581093c4a5e4e98a4bf0f9db80dfbe8_jpg.rf.dc1f17ec58e3671a7ec85d21cc5dad19.jpg", save=True, conf=0.4)