from ultralytics import YOLO

model = YOLO("runs/det_janelas2/weights/best.pt")

results = model.predict("dataset/images/test/acdaa13aed6c26a036a69f1431c77c82_jpg.rf.c260d83dfd8af011ca4ded36d3a60d4d.jpg", save=True, conf=0.1)