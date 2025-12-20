import cv2  # OpenCV kütüphanesini içe aktar (görüntü işleme için)
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar (görselleştirme için)

def show(img, title=""):  # Görüntüyü ekranda göstermek için fonksiyon tanımla
    plt.figure(figsize=(5,5))  # 5x5 inç boyutunda yeni bir figür oluştur
    if len(img.shape) == 2:  # Eğer görüntü gri tonlamalıysa (2 boyutlu)
        plt.imshow(img, cmap="gray")  # Gri renk haritasıyla göster
    else:  # Aksi halde (renkli görüntü)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # BGR'den RGB'ye çevir ve göster
    plt.title(title)  # Başlık ekle
    plt.axis("off")  # Eksenleri gizle
    plt.show()  # Görüntüyü ekranda göster

img = cv2.imread("ornek.jpg")
show(img, "Orijinal")