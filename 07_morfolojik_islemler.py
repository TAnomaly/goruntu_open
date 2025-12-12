# Morfolojik İşlemler - Dilation, Erosion, Opening, Closing
import cv2
import matplotlib.pyplot as plt

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernels = [3, 7, 11]  # Yapısal eleman boyutları

plt.figure(figsize=(12, 8))
plt.suptitle("Morfolojik İşlemler", fontweight='bold')

for i, k in enumerate(kernels):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    
    # Dilation: Beyaz alanları genişletir
    plt.subplot(3, 4, i*4 + 1)
    plt.imshow(cv2.dilate(binary, kernel), cmap="gray")
    plt.title(f"Dilation {k}x{k}"); plt.axis("off")
    
    # Erosion: Beyaz alanları küçültür
    plt.subplot(3, 4, i*4 + 2)
    plt.imshow(cv2.erode(binary, kernel), cmap="gray")
    plt.title(f"Erosion {k}x{k}"); plt.axis("off")
    
    # Opening: Erosion→Dilation (küçük gürültü temizler)
    plt.subplot(3, 4, i*4 + 3)
    plt.imshow(cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel), cmap="gray")
    plt.title(f"Opening {k}x{k}"); plt.axis("off")
    
    # Closing: Dilation→Erosion (küçük delikleri doldurur)
    plt.subplot(3, 4, i*4 + 4)
    plt.imshow(cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel), cmap="gray")
    plt.title(f"Closing {k}x{k}"); plt.axis("off")

plt.tight_layout()
plt.show()