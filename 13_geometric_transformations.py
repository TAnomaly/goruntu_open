import cv2  # OpenCV kütüphanesini içe aktar
import numpy as np  # NumPy kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

img = cv2.imread("harita.png")  # Harita görüntüsünü dosyadan oku
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Gri tonlamaya çevir

emboss_kernel_1 = np.array([[-2, -1, 0],  # Emboss filtresi 1 - Güneydoğu yönü
                            [-1, 1, 1],
                            [0, 1, 2]])

emboss_kernel_2 = np.array([[0, -1, -1],  # Emboss filtresi 2 - Kuzeybatı yönü
                            [1, 0, -1],
                            [1, 1, 0]])

emboss_kernel_3 = np.array([[-1, -1, 0],  # Emboss filtresi 3 - Köşegen yönü
                            [-1, 0, 1],
                            [0, 1, 1]])

emboss1 = cv2.filter2D(gray, -1, emboss_kernel_1)  # Birinci emboss filtresini uygula
emboss2 = cv2.filter2D(gray, -1, emboss_kernel_2)  # İkinci emboss filtresini uygula
emboss3 = cv2.filter2D(gray, -1, emboss_kernel_3)  # Üçüncü emboss filtresini uygula

emboss1_offset = np.clip(emboss1 + 128, 0, 255).astype(np.uint8)  # Gri seviyeye offset ekle (kabartma efekti)
emboss2_offset = np.clip(emboss2 + 128, 0, 255).astype(np.uint8)  # Gri seviyeye offset ekle
emboss3_offset = np.clip(emboss3 + 128, 0, 255).astype(np.uint8)  # Gri seviyeye offset ekle

emboss_color = cv2.filter2D(img, -1, emboss_kernel_1)  # Renkli görüntüye emboss uygula
emboss_color_offset = np.clip(emboss_color.astype(np.int16) + 128, 0, 255).astype(np.uint8)  # Offset ekle

plt.figure(figsize=(14, 8))  # 14x8 inç boyutunda figür oluştur
plt.suptitle("GNSS Harita - Emboss/Kabartma Efektleri", fontweight='bold', fontsize=14)  # Ana başlık

plt.subplot(2, 3, 1)  # İlk alt grafik
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Orijinal haritayı göster
plt.title("Orijinal Harita")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

plt.subplot(2, 3, 2)  # İkinci alt grafik
plt.imshow(emboss1_offset, cmap="gray")  # Güneydoğu emboss'u göster
plt.title("Emboss - Güneydoğu")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

plt.subplot(2, 3, 3)  # Üçüncü alt grafik
plt.imshow(emboss2_offset, cmap="gray")  # Kuzeybatı emboss'u göster
plt.title("Emboss - Kuzeybatı")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

plt.subplot(2, 3, 4)  # Dördüncü alt grafik
plt.imshow(emboss3_offset, cmap="gray")  # Köşegen emboss'u göster
plt.title("Emboss - Köşegen")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

plt.subplot(2, 3, 5)  # Beşinci alt grafik
plt.imshow(cv2.cvtColor(emboss_color_offset, cv2.COLOR_BGR2RGB))  # Renkli emboss'u göster
plt.title("Renkli Emboss")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

blended = cv2.addWeighted(img, 0.5, emboss_color_offset, 0.5, 0)  # Orijinal ve emboss'u karıştır
plt.subplot(2, 3, 6)  # Altıncı alt grafik
plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))  # 3D kabartmalı haritayı göster
plt.title("3D Kabartmalı Harita")  # Başlık ekle
plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster
