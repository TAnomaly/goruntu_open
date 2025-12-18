import cv2
import matplotlib.pyplot as plt

def show(img, title=""):
    plt.figure(figsize=(5,5))
    if len(img.shape) == 2:
        plt.imshow(img, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

img = cv2.imread("ornek.jpg")
show(img, "Orijinal")