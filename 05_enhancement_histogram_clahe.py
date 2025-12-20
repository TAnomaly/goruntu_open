import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir

hist_eq = cv2.equalizeHist(gray)  # Histogram eşitleme uygula

clips = [1.0, 2.0, 4.0]  # CLAHE için clip limit değerleri

plt.figure(figsize=(14, 4))  # 14x4 inç boyutunda figür oluştur
plt.subplot(1, 5, 1); plt.imshow(gray, cmap="gray"); plt.title("Orijinal"); plt.axis("off")  # Orijinal görüntüyü göster
plt.subplot(1, 5, 2); plt.imshow(hist_eq, cmap="gray"); plt.title("Histogram EQ"); plt.axis("off")  # Histogram eşitlenmiş görüntü

for i, c in enumerate(clips):  # Her clip değeri için döngü
    clahe = cv2.createCLAHE(clipLimit=c, tileGridSize=(8,8))  # CLAHE nesnesi oluştur (Contrast Limited Adaptive Histogram Equalization)
    result = clahe.apply(gray)  # CLAHE uygula
    plt.subplot(1, 5, i+3)  # Alt grafiğe geç
    plt.imshow(result, cmap="gray")  # Sonucu göster
    plt.title(f"CLAHE\nclip={c}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster