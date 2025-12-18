import cv2
import matplotlib.pyplot as plt

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)

bits = [8, 4, 2, 1]

plt.figure(figsize=(12, 4))
for i, b in enumerate(bits):
    levels = 2 ** b
    step = 256 // levels
    quant = (gray // step) * step
    
    plt.subplot(1, 4, i+1)
    plt.imshow(quant, cmap="gray")
    plt.title(f"{b}-bit\n({levels} seviye)")
    plt.axis("off")

plt.tight_layout()
plt.show()
