# Detector de Face de Dado com Webcam

Este projeto implementa um detector em tempo real que identifica e conta os pontos em faces de dados usando a webcam.

## Descrição

O programa utiliza a biblioteca OpenCV para capturar imagens da webcam e aplicar algoritmos de processamento de imagem para detectar os pontos (círculos) nas faces de um dado. O valor da face é determinado pela quantidade de pontos detectados.

## Funcionalidades

- Captura de vídeo em tempo real através da webcam
- Processamento de imagem para detecção de pontos circulares
- Contagem automática dos pontos para determinar o valor da face do dado
- Exibição visual dos pontos detectados
- Visualização do valor do dado na tela

## Requisitos

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Instalação

1. Clone este repositório ou baixe o arquivo de código
2. Instale as dependências:

```bash
pip install opencv-python numpy
```

## Como usar

Execute o script Python:

```bash
python detector_dado.py
```

- A webcam será ativada automaticamente
- Posicione um dado na frente da câmera
- Os pontos detectados serão marcados em vermelho
- O valor do dado será mostrado no canto superior esquerdo
- Pressione 'q' para encerrar o programa

## Detalhes técnicos

O programa utiliza as seguintes técnicas de processamento de imagem:

1. Conversão para escala de cinza
2. Aplicação de desfoque mediano para redução de ruído
3. Detecção de blobs (pontos) utilizando `SimpleBlobDetector` com parâmetros otimizados:
   - Filtragem por área
   - Filtragem por circularidade
   - Filtragem por convexidade
   - Filtragem por inércia

## Parâmetros de detecção

Os parâmetros para o detector de blobs podem ser ajustados para melhorar a precisão em diferentes condições de iluminação e tipos de dados:

- `minArea` e `maxArea`: Controlam o tamanho dos pontos detectados
- `minCircularity`: Define o quão circular um ponto deve ser
- `minConvexity`: Controla a convexidade dos pontos
- `minInertiaRatio`: Afeta a detecção baseada na forma dos pontos

## Limitações

- A detecção pode ser afetada por condições de iluminação inadequadas
- Dados com designs não convencionais podem não ser detectados corretamente
- A precisão da detecção depende do posicionamento do dado na frente da câmera
