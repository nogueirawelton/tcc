from ultralytics import YOLO


model = YOLO('yolov8m.pt')
results = model.train(
    data="dt.yaml",
    epochs=150,            # Aumentar para mais ciclos de aprendizado
    imgsz=800,             # Aumentar para melhor precisão
    batch=8,               # Manter para equilíbrio entre precisão e memória
    name='det_all',
    project="./runs",
    degrees=20,
    flipud=0.2,            # Reduzir para evitar layouts invertidos
    fliplr=0.5,
    scale=0.5,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    mosaic=0.5,            # Reduzir para não sobrecarregar o modelo
    mixup=0.2,
    patience=20
)