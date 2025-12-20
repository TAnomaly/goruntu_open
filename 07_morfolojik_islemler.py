import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Otsu ile ikili görüntüye çevir

kernels = [3, 7, 11]  # Yapılandırma elemanı boyutları

plt.figure(figsize=(12, 8))  # 12x8 inç boyutunda figür oluştur
plt.suptitle("Morfolojik İşlemler", fontweight='bold')  # Ana başlık ekle

for i, k in enumerate(kernels):  # Her çekirdek boyutu için döngü
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))  # Dikdörtgen yapılandırma elemanı oluştur
    
    plt.subplot(3, 4, i*4 + 1)  # Dilation alt grafiği
    plt.imshow(cv2.dilate(binary, kernel), cmap="gray")  # Genişletme (dilation) uygula ve göster
    plt.title(f"Dilation {k}x{k}"); plt.axis("off")  # Başlık ekle, eksenleri gizle
    
    plt.subplot(3, 4, i*4 + 2)  # Erosion alt grafiği
    plt.imshow(cv2.erode(binary, kernel), cmap="gray")  # Aşındırma (erosion) uygula ve göster
    plt.title(f"Erosion {k}x{k}"); plt.axis("off")  # Başlık ekle, eksenleri gizle
    
    plt.subplot(3, 4, i*4 + 3)  # Opening alt grafiği
    plt.imshow(cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel), cmap="gray")  # Açma (opening) uygula ve göster
    plt.title(f"Opening {k}x{k}"); plt.axis("off")  # Başlık ekle, eksenleri gizle
    
    plt.subplot(3, 4, i*4 + 4)  # Closing alt grafiği
    plt.imshow(cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel), cmap="gray")  # Kapama (closing) uygula ve göster
    plt.title(f"Closing {k}x{k}"); plt.axis("off")  # Başlık ekle, eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster