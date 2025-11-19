import cv2 
from ultralytics import YOLO

# carregar o modelo 
model = YOLO('data/best.pt')

# inicializar câmera
cam = cv2.VideoCapture(1)

if cam.isOpened(): 
    sucess, frame = cam.read()

    while sucess: 
        validacao, frame = cam.read()

        results = model(frame, imgsz=640, verbose=False)

        # Desenhar as caixas delimitadoras e rótulos no frame
        annotated_frame = results[0].plot()

        # Mostrar o frame anotado
        cv2.imshow("YOLOv8 Detection", annotated_frame)

        key = cv2.waitKey(5) 
        if key == ord('q'):
            break 


cam.release() 
cv2.destroyAllWindows() 