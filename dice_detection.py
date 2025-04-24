import cv2
import numpy as np

def detectar_face_dado_webcam():
    """
    Usar a webcam para detectar a face do dado em tempo real
    """
    # Inicializar a webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capturar frame da webcam
        ret, frame = cap.read()
        if not ret:
            break
        
        # Processar frame para detecção
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.medianBlur(gray, 5)
        
        # Configurar parâmetros para o detector de blobs
        params = cv2.SimpleBlobDetector_Params()
        
        # Filtrar por área
        params.filterByArea = True
        params.minArea = 50
        params.maxArea = 500
        
        # Filtrar por circularidade
        params.filterByCircularity = True
        params.minCircularity = 0.7
        
        # Filtrar por convexidade
        params.filterByConvexity = True
        params.minConvexity = 0.8
        
        # Filtrar por inércia
        params.filterByInertia = True
        params.minInertiaRatio = 0.5
        
        # Criar o detector com os parâmetros
        detector = cv2.SimpleBlobDetector_create(params)
        
        # Detectar blobs (pontos do dado)
        keypoints = detector.detect(blurred)
        
        # Contar keypoints para determinar o valor da face
        valor_dado = len(keypoints)
        
        # Desenhar keypoints na imagem
        img_com_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), 
                                              (0, 0, 255), 
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        # Mostrar o valor do dado na imagem
        cv2.putText(img_com_keypoints, f"Valor do dado: {valor_dado}", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Exibir o resultado
        cv2.imshow("Detecção de Dado", img_com_keypoints)
        
        # Sair com a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detectar_face_dado_webcam()
