from ultralytics import YOLO
# room_model = YOLO('yolov8n.pt')
# room_model.train(
#     data="dt.yaml",
#     epochs=150,
#     imgsz=960,
#     batch=16,
#     mosaic=0.5,
#     mixup=0.0,
#     degrees=2,
#     scale=0.3,
#     hsv_h=0.01,
#     hsv_s=0.5,
#     hsv_v=0.4,
#     classes=[0],
# )

window_model = YOLO('yolov8n.pt')
window_model.train(
    data="dt.yaml",
    epochs=150,               # Aumentar para mais épocas
    imgsz=960,                # Aumentar resolução para mais detalhes
    batch=32,                 # Aumentar batch size para melhorar a convergência
    name='det_windows',
    project="./runs",
    degrees=5,                # Manter rotação baixa
    flipud=0.0,
    fliplr=0.2,               # Reduzir flip horizontal
    scale=0.1,                # Reduzir variação de escala
    hsv_h=0.0,
    hsv_s=0.1,
    hsv_v=0.2,
    mosaic=0.2,               # Ativar mosaic com intensidade baixa
    mixup=0.0,                # Desativar mixup
    patience=20,              # Deixar paciência alta
    conf=0.3,                 # Aumentar recall com confiança mais baixa
    iou=0.5,                  # Maior IOU para reduzir múltiplas caixas sobrepostas
    classes=[1],              # Apenas janelas
)
