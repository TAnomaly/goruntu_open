# Edge Detection - Kenar Tespiti
import cv2
import matplotlib.pyplot as plt
import numpy as np

gray = cv2.cvtColor(cv2.imread("ornek.jpg"), cv2.COLOR_BGR2GRAY)

canny_params = [(50, 100), (100, 200), (150, 300)]  # (alt eşik, üst eşik)

plt.figure(figsize=(12, 6))

# Canny: En popüler kenar bulucu (çift eşikli)
for i, (low, high) in enumerate(canny_params):
    edges = cv2.Canny(gray, low, high)
    plt.subplot(2, 4, i+1)
    plt.imshow(edges, cmap="gray")
    plt.title(f"Canny\n{low}-{high}")
    plt.axis("off")

# Sobel: Yön bazlı türev (X=dikey, Y=yatay kenarlar)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # X yönü
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Y yönü
sobel = cv2.magnitude(sobelx, sobely)  # Birleşik

plt.subplot(2, 4, 4); plt.imshow(np.abs(sobelx), cmap="gray"); plt.title("Sobel X"); plt.axis("off")
plt.subplot(2, 4, 5); plt.imshow(np.abs(sobely), cmap="gray"); plt.title("Sobel Y"); plt.axis("off")
plt.subplot(2, 4, 6); plt.imshow(sobel, cmap="gray"); plt.title("Sobel Combined"); plt.axis("off")

# Laplacian: 2. türev (tüm yönlerde kenar)
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
plt.subplot(2, 4, 7); plt.imshow(np.abs(laplacian), cmap="gray"); plt.title("Laplacian"); plt.axis("off")

plt.tight_layout()
plt.show()