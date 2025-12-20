import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir

kernels = [3, 5, 7, 11]  # Filtre çekirdek boyutları

plt.figure(figsize=(14, 6))  # 14x6 inç boyutunda figür oluştur
plt.suptitle("Gaussian (üst) vs Median (alt) Filtre", fontweight='bold')  # Ana başlık ekle

for i, k in enumerate(kernels):  # Her çekirdek boyutu için döngü
    gauss = cv2.GaussianBlur(gray, (k, k), 0)  # Gaussian bulanıklaştırma uygula
    plt.subplot(2, 4, i+1)  # Üst satır alt grafik
    plt.imshow(gauss, cmap="gray")  # Gaussian sonucunu göster
    plt.title(f"Gaussian {k}x{k}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle
    
    median = cv2.medianBlur(gray, k)  # Median filtresi uygula
    plt.subplot(2, 4, i+5)  # Alt satır alt grafik
    plt.imshow(median, cmap="gray")  # Median sonucunu göster
    plt.title(f"Median {k}x{k}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster