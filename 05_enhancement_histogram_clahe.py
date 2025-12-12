# Enhancement - Histogram Equalization ve CLAHE
import cv2
import matplotlib.pyplot as plt

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)

hist_eq = cv2.equalizeHist(gray)  # Global kontrast artırma

clips = [1.0, 2.0, 4.0]  # CLAHE kırpma limitleri (arttıkça kontrast artar)

plt.figure(figsize=(14, 4))
plt.subplot(1, 5, 1); plt.imshow(gray, cmap="gray"); plt.title("Orijinal"); plt.axis("off")
plt.subplot(1, 5, 2); plt.imshow(hist_eq, cmap="gray"); plt.title("Histogram EQ"); plt.axis("off")

for i, c in enumerate(clips):
    # CLAHE: Lokal histogram eşitleme (daha doğal sonuç)
    clahe = cv2.createCLAHE(clipLimit=c, tileGridSize=(8,8))
    result = clahe.apply(gray)
    plt.subplot(1, 5, i+3)
    plt.imshow(result, cmap="gray")
    plt.title(f"CLAHE\nclip={c}")
    plt.axis("off")

plt.tight_layout()
plt.show()