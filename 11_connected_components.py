import cv2
import matplotlib.pyplot as plt

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)

thresholds = [50, 100, 150, 200]

plt.figure(figsize=(12, 6))

for i, t in enumerate(thresholds):
    _, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    
    num_labels, labels = cv2.connectedComponents(binary)
    
    plt.subplot(2, 4, i+1)
    plt.imshow(binary, cmap="gray")
    plt.title(f"Binary\nthresh={t}")
    plt.axis("off")
    
    plt.subplot(2, 4, i+5)
    plt.imshow(labels, cmap="nipy_spectral")
    plt.title(f"{num_labels} bileşen")
    plt.axis("off")

plt.tight_layout()
plt.show()