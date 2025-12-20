import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

img = cv2.imread("ornek.jpg")  # Görüntüyü dosyadan oku
h, w = img.shape[:2]  # Görüntünün yükseklik ve genişliğini al

factors = [2, 4, 8]  # Örnekleme faktörleri listesi

plt.figure(figsize=(12, 4))  # 12x4 inç boyutunda figür oluştur
plt.subplot(1, 4, 1)  # 1x4 grid'de 1. alt grafik
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Orijinal görüntüyü göster
plt.title(f"Orijinal\n{w}x{h}")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

for i, f in enumerate(factors):  # Her örnekleme faktörü için döngü
    small = cv2.resize(img, (w//f, h//f), interpolation=cv2.INTER_NEAREST)  # Görüntüyü küçült
    big = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)  # Tekrar büyüt (pikselleşme göster)
    
    plt.subplot(1, 4, i+2)  # Sonraki alt grafiğe geç
    plt.imshow(cv2.cvtColor(big, cv2.COLOR_BGR2RGB))  # Örneklenmiş görüntüyü göster
    plt.title(f"1/{f} Örnekleme\n{w//f}x{h//f}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster