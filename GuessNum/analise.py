import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


def analisar_imagem():
    
    modelo = load_model("cachola.keras")
   
    img = cv2.imread("process/process.png", cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, (28, 28))  
    img = img / 255.0  
    
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)

    previsao = modelo.predict(img)
    numero_previsto = np.argmax(previsao)

    print(f"O número é: {numero_previsto}")


analisar_imagem()
