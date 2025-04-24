# Detector de Faces de Dados

Este projeto utiliza visão computacional para detectar e contar o valor das faces de um dado em tempo real usando a webcam. O sistema identifica os pontos (dots) presentes na face do dado e determina seu valor.

## Funcionalidades

- Detecção em tempo real da face do dado através da webcam
- Identificação do número de pontos na face do dado
- Interface visual com quadrado para posicionamento do dado
- Visualização da máscara de processamento
- Detecção da face do dado com base na cor e formato

## Dependências

O projeto requer as seguintes bibliotecas Python:
- OpenCV (cv2): para processamento de imagem e visão computacional
- NumPy: para operações com arrays e matrizes

## Instalação

1. Certifique-se de ter Python 3.6+ instalado
2. Instale as dependências:

```bash
pip install opencv-python numpy
```

## Como Usar

1. Execute o script principal:

```bash
python detector_dado.py
```

2. Uma janela será aberta mostrando a imagem da webcam
3. Posicione um dado dentro do quadrado verde
4. O sistema detectará automaticamente a face do dado e contará os pontos
5. Pressione 'q' ou 'Q' para sair do programa

## Explicação do Código

O código utiliza as seguintes técnicas de processamento de imagem:

1. **Captura de vídeo**: Acessa a webcam para obter os frames
2. **Região de interesse (ROI)**: Define um quadrado no centro da imagem
3. **Detecção de blobs**: Identifica os pontos (dots) do dado
4. **Segmentação por cor**: Usa espaço de cor HSV para detectar a face branca do dado
5. **Morfologia matemática**: Aplica operações de abertura e fechamento para melhorar a máscara
6. **Detecção de contornos**: Identifica o contorno da face do dado
7. **Validação geométrica**: Verifica se o contorno tem proporções adequadas para ser um dado

## Parâmetros Configuráveis

Vários parâmetros podem ser ajustados para melhorar a detecção:

- `params.minArea` e `params.maxArea`: Área mínima e máxima dos blobs (pontos)
- `params.minCircularity`: Circularidade mínima dos blobs
- `params.minConvexity`: Convexidade mínima dos blobs
- `params.minInertiaRatio`: Razão de inércia mínima dos blobs
- `lower_white` e `upper_white`: Limites para detecção da cor branca no espaço HSV
- `min_area`: Área mínima do contorno para ser considerado uma face de dado
