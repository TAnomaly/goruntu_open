# Görüntü Yükleme ve Gösterme
import cv2
import matplotlib.pyplot as plt

def show(img, title=""):
    """BGR görüntüyü matplotlib ile göster"""
    plt.figure(figsize=(5,5))
    if len(img.shape) == 2:  # Gri tonlu
        plt.imshow(img, cmap="gray")
    else:  # Renkli (BGR→RGB çevir)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

img = cv2.imread("ornek.jpg")  # Görüntüyü BGR olarak oku
show(img, "Orijinal")