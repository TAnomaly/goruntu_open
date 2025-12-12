# Thresholding - Görüntüyü binary (siyah-beyaz) yapma
import cv2
import matplotlib.pyplot as plt

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)

thresholds = [50, 100, 150, 200]  # Eşik değerleri

plt.figure(figsize=(14, 6))

# Global threshold: Piksel > eşik → beyaz, değilse → siyah
for i, t in enumerate(thresholds):
    _, th = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    plt.subplot(2, 5, i+1)
    plt.imshow(th, cmap="gray")
    plt.title(f"Global\nthresh={t}")
    plt.axis("off")

# Otsu: Otomatik en iyi eşiği bulur
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.subplot(2, 5, 5)
plt.imshow(otsu, cmap="gray")
plt.title("Otsu\n(otomatik)")
plt.axis("off")

# Adaptive: Her bölge için ayrı eşik (ışık değişimine dayanıklı)
blocks = [5, 11, 21, 51]
for i, b in enumerate(blocks):
    adapt = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, b, 2)
    plt.subplot(2, 5, i+6)
    plt.imshow(adapt, cmap="gray")
    plt.title(f"Adaptive\nblock={b}")
    plt.axis("off")

plt.tight_layout()
plt.show()