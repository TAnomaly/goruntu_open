# Deep Learning Segmentasyon - DeepLabv3 ile piksel bazlı sınıflandırma
import torch
import torchvision
from PIL import Image
import matplotlib.pyplot as plt

# Önceden eğitilmiş model yükle (COCO: 21 sınıf)
model = torchvision.models.segmentation.deeplabv3_resnet50(pretrained=True)
model.eval()

# Görüntüyü yükle ve normalize et
img = Image.open("ornek.jpg").convert("RGB")
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
inp = transform(img).unsqueeze(0)  # Batch boyutu ekle

# Model çıkarımı
with torch.no_grad():
    out = model(inp)["out"][0]
mask = out.argmax(0).cpu().numpy()  # Her piksel için en olası sınıf

# Gösterim
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1); plt.imshow(img); plt.title("Orijinal"); plt.axis("off")
plt.subplot(1, 3, 2); plt.imshow(mask, cmap="tab20"); plt.title("Maske"); plt.axis("off")
plt.subplot(1, 3, 3); plt.imshow(img); plt.imshow(mask, alpha=0.5, cmap="tab20"); plt.title("Overlay"); plt.axis("off")
plt.tight_layout()
plt.show()