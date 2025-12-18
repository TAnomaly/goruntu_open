import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ornek.jpg")
Z = img.reshape((-1, 3)).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

k_values = [2, 4, 8, 16]

plt.figure(figsize=(14, 4))
plt.subplot(1, 5, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Orijinal")
plt.axis("off")

for i, K in enumerate(k_values):
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    segmented = centers[labels.flatten()].reshape(img.shape)
    
    plt.subplot(1, 5, i+2)
    plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
    plt.title(f"K = {K}")
    plt.axis("off")

plt.tight_layout()
plt.show()