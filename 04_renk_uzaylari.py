import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

img = cv2.imread("ornek.jpg")  # Görüntüyü dosyadan oku
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Gri tonlamaya çevir
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # HSV renk uzayına çevir

plt.figure(figsize=(12, 6))  # 12x6 inç boyutunda figür oluştur

plt.subplot(2, 4, 1); plt.imshow(rgb); plt.title("RGB"); plt.axis("off")  # RGB görüntüyü göster
plt.subplot(2, 4, 2); plt.imshow(gray, cmap="gray"); plt.title("Grayscale"); plt.axis("off")  # Gri görüntüyü göster

plt.subplot(2, 4, 3); plt.imshow(rgb[:,:,0], cmap="Reds"); plt.title("R Kanalı"); plt.axis("off")  # Kırmızı kanalı göster
plt.subplot(2, 4, 4); plt.imshow(rgb[:,:,1], cmap="Greens"); plt.title("G Kanalı"); plt.axis("off")  # Yeşil kanalı göster

plt.subplot(2, 4, 5); plt.imshow(hsv[:,:,0], cmap="hsv"); plt.title("H (Renk Tonu)"); plt.axis("off")  # Hue kanalını göster
plt.subplot(2, 4, 6); plt.imshow(hsv[:,:,1], cmap="gray"); plt.title("S (Doygunluk)"); plt.axis("off")  # Saturation kanalını göster
plt.subplot(2, 4, 7); plt.imshow(hsv[:,:,2], cmap="gray"); plt.title("V (Parlaklık)"); plt.axis("off")  # Value kanalını göster
plt.subplot(2, 4, 8); plt.imshow(rgb[:,:,2], cmap="Blues"); plt.title("B Kanalı"); plt.axis("off")  # Mavi kanalı göster

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster