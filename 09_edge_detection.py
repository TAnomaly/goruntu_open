import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar
import numpy as np  # NumPy kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir

canny_params = [(50, 100), (100, 200), (150, 300)]  # Canny kenar algılama parametreleri (düşük, yüksek eşik)

plt.figure(figsize=(12, 6))  # 12x6 inç boyutunda figür oluştur

for i, (low, high) in enumerate(canny_params):  # Her parametre çifti için döngü
    edges = cv2.Canny(gray, low, high)  # Canny kenar algılama uygula
    plt.subplot(2, 4, i+1)  # Alt grafiğe geç
    plt.imshow(edges, cmap="gray")  # Kenarları göster
    plt.title(f"Canny\n{low}-{high}")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X yönünde türev (yatay kenarlar)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y yönünde türev (dikey kenarlar)
sobel = cv2.magnitude(sobelx, sobely)  # Sobel büyüklüğü (toplam gradyan)

plt.subplot(2, 4, 4); plt.imshow(np.abs(sobelx), cmap="gray"); plt.title("Sobel X"); plt.axis("off")  # Sobel X göster
plt.subplot(2, 4, 5); plt.imshow(np.abs(sobely), cmap="gray"); plt.title("Sobel Y"); plt.axis("off")  # Sobel Y göster
plt.subplot(2, 4, 6); plt.imshow(sobel, cmap="gray"); plt.title("Sobel Combined"); plt.axis("off")  # Birleşik Sobel göster

laplacian = cv2.Laplacian(gray, cv2.CV_64F)  # Laplacian operatörü (ikinci türev)
plt.subplot(2, 4, 7); plt.imshow(np.abs(laplacian), cmap="gray"); plt.title("Laplacian"); plt.axis("off")  # Laplacian göster

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster