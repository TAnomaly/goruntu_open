# Restorasyon - Gaussian ve Median Filtre (Gürültü Azaltma)
import cv2
import matplotlib.pyplot as plt

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)

kernels = [3, 5, 7, 11]  # Filtre boyutları (büyükse daha bulanık)

plt.figure(figsize=(14, 6))
plt.suptitle("Gaussian (üst) vs Median (alt) Filtre", fontweight='bold')

for i, k in enumerate(kernels):
    # Gaussian: Genel yumuşatma (kenarları da bulanıklaştırır)
    gauss = cv2.GaussianBlur(gray, (k, k), 0)
    plt.subplot(2, 4, i+1)
    plt.imshow(gauss, cmap="gray")
    plt.title(f"Gaussian {k}x{k}")
    plt.axis("off")
    
    # Median: Tuz-biber gürültüsü için ideal (kenarları korur)
    median = cv2.medianBlur(gray, k)
    plt.subplot(2, 4, i+5)
    plt.imshow(median, cmap="gray")
    plt.title(f"Median {k}x{k}")
    plt.axis("off")

plt.tight_layout()
plt.show()