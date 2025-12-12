# Renk Uzayları - RGB, Grayscale, HSV
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ornek.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # Ekran için RGB
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Tek kanal (parlaklık)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # Renk tonu + doygunluk + parlaklık

plt.figure(figsize=(12, 6))

# Ana görüntüler
plt.subplot(2, 4, 1); plt.imshow(rgb); plt.title("RGB"); plt.axis("off")
plt.subplot(2, 4, 2); plt.imshow(gray, cmap="gray"); plt.title("Grayscale"); plt.axis("off")

# RGB ayrı kanallar
plt.subplot(2, 4, 3); plt.imshow(rgb[:,:,0], cmap="Reds"); plt.title("R Kanalı"); plt.axis("off")
plt.subplot(2, 4, 4); plt.imshow(rgb[:,:,1], cmap="Greens"); plt.title("G Kanalı"); plt.axis("off")

# HSV ayrı kanallar
plt.subplot(2, 4, 5); plt.imshow(hsv[:,:,0], cmap="hsv"); plt.title("H (Renk Tonu)"); plt.axis("off")
plt.subplot(2, 4, 6); plt.imshow(hsv[:,:,1], cmap="gray"); plt.title("S (Doygunluk)"); plt.axis("off")
plt.subplot(2, 4, 7); plt.imshow(hsv[:,:,2], cmap="gray"); plt.title("V (Parlaklık)"); plt.axis("off")
plt.subplot(2, 4, 8); plt.imshow(rgb[:,:,2], cmap="Blues"); plt.title("B Kanalı"); plt.axis("off")

plt.tight_layout()
plt.show()