import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir

thresholds = [50, 100, 150, 200]  # Eşik değerleri listesi

plt.figure(figsize=(12, 6))  # 12x6 inç boyutunda figür oluştur

for i, t in enumerate(thresholds):  # Her eşik değeri için döngü
    _, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)  # İkili görüntü oluştur
    
    num_labels, labels = cv2.connectedComponents(binary)  # Bağlı bileşen analizi yap
    
    plt.subplot(2, 4, i+1)  # Üst satır alt grafik
    plt.imshow(binary, cmap="gray")  # İkili görüntüyü göster
    plt.title(f"Binary\nthresh={t}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle
    
    plt.subplot(2, 4, i+5)  # Alt satır alt grafik
    plt.imshow(labels, cmap="nipy_spectral")  # Etiketlenmiş bileşenleri renkli göster
    plt.title(f"{num_labels} bileşen")  # Bileşen sayısını göster
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster