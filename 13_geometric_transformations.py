import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("harita.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

emboss_kernel_1 = np.array([[-2, -1, 0],
                            [-1, 1, 1],
                            [0, 1, 2]])

emboss_kernel_2 = np.array([[0, -1, -1],
                            [1, 0, -1],
                            [1, 1, 0]])

emboss_kernel_3 = np.array([[-1, -1, 0],
                            [-1, 0, 1],
                            [0, 1, 1]])

emboss1 = cv2.filter2D(gray, -1, emboss_kernel_1)
emboss2 = cv2.filter2D(gray, -1, emboss_kernel_2)
emboss3 = cv2.filter2D(gray, -1, emboss_kernel_3)

emboss1_offset = np.clip(emboss1 + 128, 0, 255).astype(np.uint8)
emboss2_offset = np.clip(emboss2 + 128, 0, 255).astype(np.uint8)
emboss3_offset = np.clip(emboss3 + 128, 0, 255).astype(np.uint8)

emboss_color = cv2.filter2D(img, -1, emboss_kernel_1)
emboss_color_offset = np.clip(emboss_color.astype(np.int16) + 128, 0, 255).astype(np.uint8)

plt.figure(figsize=(14, 8))
plt.suptitle("GNSS Harita - Emboss/Kabartma Efektleri", fontweight='bold', fontsize=14)

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Orijinal Harita")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(emboss1_offset, cmap="gray")
plt.title("Emboss - Güneydoğu")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(emboss2_offset, cmap="gray")
plt.title("Emboss - Kuzeybatı")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(emboss3_offset, cmap="gray")
plt.title("Emboss - Köşegen")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(emboss_color_offset, cv2.COLOR_BGR2RGB))
plt.title("Renkli Emboss")
plt.axis("off")

blended = cv2.addWeighted(img, 0.5, emboss_color_offset, 0.5, 0)
plt.subplot(2, 3, 6)
plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
plt.title("3D Kabartmalı Harita")
plt.axis("off")

plt.tight_layout()
plt.show()
