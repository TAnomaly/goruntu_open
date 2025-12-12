# Örnekleme (Sampling) - Çözünürlük azaltma
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ornek.jpg")
h, w = img.shape[:2]  # Yükseklik ve genişlik

factors = [2, 4, 8]  # Küçültme oranları

plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(f"Orijinal\n{w}x{h}")
plt.axis("off")

for i, f in enumerate(factors):
    # Küçült (örnekleme azalt)
    small = cv2.resize(img, (w//f, h//f), interpolation=cv2.INTER_NEAREST)
    # Tekrar büyüt (pikselleşme görülür)
    big = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    
    plt.subplot(1, 4, i+2)
    plt.imshow(cv2.cvtColor(big, cv2.COLOR_BGR2RGB))
    plt.title(f"1/{f} Örnekleme\n{w//f}x{h//f}")
    plt.axis("off")

plt.tight_layout()
plt.show()