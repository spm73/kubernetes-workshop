import os
import time

from ultralytics import YOLO
import cv2
import paho.mqtt.client as mqtt

CAMERA_URL = os.getenv('CAMERA_STREAM_URL', 0)
MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'localhost')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'aula/alertas/gatos')

def main():
    print("=== Arrancando Cerebro de Visión IA (YOLOv8) ===")
    print("⏳ Cargando modelo YOLOv8 Nano...")
    model = YOLO('yolov8n.pt') 
    print("✅ Modelo cargado y listo.")

    # ==========================================
    # CONEXIÓN MQTT Y CÁMARA
    # ==========================================
    client = mqtt.Client()  
    try:
        client.connect(MQTT_BROKER_URL, MQTT_PORT, 60)
        client.loop_start()
        print("✅ Conectado a MQTT.")
    except Exception as e:
        print(f"❌ Error MQTT: {e}")
        exit(1)

    cap = cv2.VideoCapture(CAMERA_URL)
    if not cap.isOpened():
        print("❌ Error fatal: No se pudo acceder a la cámara.")
        exit(1)

    print("✅ Cámara conectada. Buscando gatos...")

    tiempo_ultimo_aviso = 0

    # ==========================================
    # BUCLE PRINCIPAL DE VISIÓN
    # ==========================================
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                time.sleep(1)
                continue

            # Le pasamos la imagen a YOLO (verbose=False para no ensuciar la terminal)
            # classes=[15] le dice a YOLO que SOLO busque la clase 15 (Gato en el dataset COCO)
            resultados = model(frame, classes=[15], verbose=False)
            
            gato_detectado = False
            
            # Analizamos los resultados de la foto
            for resultado in resultados:
                if len(resultado.boxes) > 0: # Si hay al menos una "caja" detectada...
                    gato_detectado = True
                    break 

            # --- GESTIÓN DE ALERTAS ---
            if gato_detectado:
                tiempo_actual = time.time()
                if tiempo_actual - tiempo_ultimo_aviso > 5: # Aviso cada 5 segundos máximo
                    print("🐈 ¡Alerta! Se ha detectado un gato en el aula.")
                    client.publish(MQTT_TOPIC, "ON")
                    tiempo_ultimo_aviso = tiempo_actual

            # Dormimos el script 1 segundo antes de pedir la siguiente foto
            time.sleep(1)

    except KeyboardInterrupt:
        print("Apagando...")
    finally:
        cap.release()
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
