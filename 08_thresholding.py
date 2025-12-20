import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir

thresholds = [50, 100, 150, 200]  # Eşik değerleri listesi

plt.figure(figsize=(14, 6))  # 14x6 inç boyutunda figür oluştur

for i, t in enumerate(thresholds):  # Her eşik değeri için döngü
    _, th = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)  # Global eşikleme uygula
    plt.subplot(2, 5, i+1)  # Alt grafiğe geç
    plt.imshow(th, cmap="gray")  # Eşiklenmiş görüntüyü göster
    plt.title(f"Global\nthresh={t}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Otsu otomatik eşikleme
plt.subplot(2, 5, 5)  # 5. alt grafik
plt.imshow(otsu, cmap="gray")  # Otsu sonucunu göster
plt.title("Otsu\n(otomatik)")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

blocks = [5, 11, 21, 51]  # Adaptif eşikleme için blok boyutları
for i, b in enumerate(blocks):  # Her blok boyutu için döngü
    adapt = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # Adaptif Gaussian eşikleme
                                   cv2.THRESH_BINARY, b, 2)  # Blok boyutu ve sabit değer
    plt.subplot(2, 5, i+6)  # Alt satır alt grafikleri
    plt.imshow(adapt, cmap="gray")  # Adaptif sonucu göster
    plt.title(f"Adaptive\nblock={b}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster