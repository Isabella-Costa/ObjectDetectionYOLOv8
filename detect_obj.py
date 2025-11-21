import cv2
import time
from ultralytics import YOLO

pTime = 0 # Variável para armazenar o tempo anterior (para cálculo de FPS)

try:
    model = YOLO('data/best4.pt')
    model.to('cuda') # usa GPU 
except Exception as e:
    print(f"Erro ao carregar o modelo YOLO: {e}")
    exit()


cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Erro ao abrir a câmera. Verifique a conexão.")
    exit()

while True:
    sucess, frame = cam.read()
    if not sucess:
        print("Falha ao capturar frame.")
        break

    # verbose=False para suprimir a saída do terminal a cada inferência
    results = model.predict(frame, imgsz=640, half=True, verbose=False) 

    annotated_frame = results[0].plot()

    # Cálculo do FPS
    cTime = time.time()
    # O FPS = 1 / (diferença de tempo)
    fps_real = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(annotated_frame, f'FPS: {int(fps_real)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


print("Gravação finalizada.")
cam.release() # Libera a câmera
cv2.destroyAllWindows()
