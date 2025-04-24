import cv2
import numpy as np

def detectar_face_dado_webcam():
    """
    Usar a webcam para detectar a face do dado em tempo real
    com um quadrado central para facilitar o posicionamento
    """

    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar o vídeo")
        return
        
    altura, largura = frame.shape[:2]
    
    tamanho_quadrado = int(min(altura, largura) * 0.4)
    
    x_inicio = (largura - tamanho_quadrado) // 2
    y_inicio = (altura - tamanho_quadrado) // 2
    x_fim = x_inicio + tamanho_quadrado
    y_fim = y_inicio + tamanho_quadrado
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.rectangle(frame, (x_inicio, y_inicio), (x_fim, y_fim), (0, 255, 0), 2)
        
        roi = frame[y_inicio:y_fim, x_inicio:x_fim].copy()
        
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blurred_roi = cv2.medianBlur(gray_roi, 5)
        
        params = cv2.SimpleBlobDetector_Params()
        
        params.filterByArea = True
        params.minArea = 30
        params.maxArea = 500
        
        params.filterByCircularity = True
        params.minCircularity = 0.6
        
        params.filterByConvexity = True
        params.minConvexity = 0.7
        
        params.filterByInertia = True
        params.minInertiaRatio = 0.4
        
        detector = cv2.SimpleBlobDetector_create(params)
        
        keypoints = detector.detect(blurred_roi)
        
        valor_dado = len(keypoints)
        
        roi_com_keypoints = cv2.drawKeypoints(roi, keypoints, np.array([]), 
                                              (0, 0, 255), 
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        lower_white = np.array([0, 0, 150])
        upper_white = np.array([180, 60, 255])
        
      
        mask_white = cv2.inRange(hsv, lower_white, upper_white)
        
     
        kernel = np.ones((5, 5), np.uint8)
        mask_white = cv2.morphologyEx(mask_white, cv2.MORPH_OPEN, kernel)
        mask_white = cv2.morphologyEx(mask_white, cv2.MORPH_CLOSE, kernel)
        
      
        contornos, _ = cv2.findContours(mask_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
   
        for contorno in contornos:
         
            area = cv2.contourArea(contorno)
            
         
            min_area = 1000 
            if area > min_area:
               
                x, y, w, h = cv2.boundingRect(contorno)
                
            
                ratio = float(w) / h
                if 0.7 <= ratio <= 1.3:
                    
                    cv2.rectangle(roi_com_keypoints, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    
                   
                    cv2.putText(roi_com_keypoints, "Face do Dado", 
                                (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        
        mask_small = cv2.resize(mask_white, (tamanho_quadrado//4, tamanho_quadrado//4))
        
        mask_small_bgr = cv2.cvtColor(mask_small, cv2.COLOR_GRAY2BGR)
        
        roi_com_keypoints[0:tamanho_quadrado//4, tamanho_quadrado-tamanho_quadrado//4:tamanho_quadrado] = mask_small_bgr
        
        frame[y_inicio:y_fim, x_inicio:x_fim] = roi_com_keypoints
        
        cv2.putText(frame, f"Valor do dado: {valor_dado}", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("Deteccao de Dado", frame)
        
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord('q') or tecla == ord('Q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_face_dado_webcam()