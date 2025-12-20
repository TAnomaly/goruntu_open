import torch  # PyTorch kütüphanesini içe aktar
import torchvision  # Torchvision kütüphanesini içe aktar (önceden eğitilmiş modeller için)
from PIL import Image  # PIL kütüphanesini içe aktar (görüntü yükleme için)
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini içe aktar

model = torchvision.models.segmentation.deeplabv3_resnet50(pretrained=True)  # Önceden eğitilmiş DeepLabV3 modelini yükle
model.eval()  # Modeli değerlendirme moduna al

img = Image.open("ornek.jpg").convert("RGB")  # Görüntüyü aç ve RGB'ye çevir
transform = torchvision.transforms.Compose([  # Dönüşüm pipeline'ı oluştur
    torchvision.transforms.ToTensor(),  # Görüntüyü tensöre çevir
    torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # ImageNet ortalaması ile normalize et
])
inp = transform(img).unsqueeze(0)  # Batch boyutu ekle

with torch.no_grad():  # Gradyan hesaplamayı devre dışı bırak (çıkarım modu)
    out = model(inp)["out"][0]  # Modelden çıktı al
mask = out.argmax(0).cpu().numpy()  # En yüksek olasılıklı sınıfı seç (segmentasyon maskesi)

plt.figure(figsize=(12, 4))  # 12x4 inç boyutunda figür oluştur
plt.subplot(1, 3, 1); plt.imshow(img); plt.title("Orijinal"); plt.axis("off")  # Orijinal görüntüyü göster
plt.subplot(1, 3, 2); plt.imshow(mask, cmap="tab20"); plt.title("Maske"); plt.axis("off")  # Segmentasyon maskesini göster
plt.subplot(1, 3, 3); plt.imshow(img); plt.imshow(mask, alpha=0.5, cmap="tab20"); plt.title("Overlay"); plt.axis("off")  # Üzerine bindirme göster
plt.tight_layout()  # Alt grafikleri düzenle
plt.show()  # Tüm grafikleri göster