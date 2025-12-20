import cv2  # OpenCV kütüphanesini içe aktar
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)  # Görüntüyü oku ve gri tonlamaya çevir

bits = [8, 4, 2, 1]  # Bit derinlikleri listesi

plt.figure(figsize=(12, 4))  # 12x4 inç boyutunda figür oluştur
for i, b in enumerate(bits):  # Her bit derinliği için döngü
    levels = 2 ** b  # Seviye sayısını hesapla (2^bit)
    step = 256 // levels  # Adım büyüklüğünü hesapla
    quant = (gray // step) * step  # Kuantalama uygula (renk seviyelerini azalt)
    
    plt.subplot(1, 4, i+1)  # Alt grafiğe geç
    plt.imshow(quant, cmap="gray")  # Kuantalanmış görüntüyü göster
    plt.title(f"{b}-bit\n({levels} seviye)")  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle

plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster
