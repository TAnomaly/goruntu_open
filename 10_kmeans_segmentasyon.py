import cv2  # OpenCV kütüphanesini içe aktar
import numpy as np  # NumPy kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

img = cv2.imread("ornek.jpg")  # Görüntüyü dosyadan oku
Z = img.reshape((-1, 3)).astype(np.float32)  # Görüntüyü piksel listesine dönüştür (her piksel 3 renk değeri)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)  # K-means durma kriteri (epsilon + max iterasyon)

k_values = [2, 4, 8, 16]  # Küme sayıları (K değerleri)

plt.figure(figsize=(14, 4))  # 14x4 inç boyutunda figür oluştur
plt.subplot(1, 5, 1)  # İlk alt grafik
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Orijinal görüntüyü göster
plt.title("Orijinal")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

for i, K in enumerate(k_values):  # Her K değeri için döngü
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)  # K-means kümeleme uygula
    centers = np.uint8(centers)  # Merkez değerlerini tam sayıya çevir
    segmented = centers[labels.flatten()].reshape(img.shape)  # Segmente edilmiş görüntüyü oluştur
    
    plt.subplot(1, 5, i+2)  # Alt grafiğe geç
    plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))  # Segmente görüntüyü göster
    plt.title(f"K = {K}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster