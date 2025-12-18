# Görüntü İşleme - Matematiksel Formüller

## 1. Görüntü Yükleme ve Temel Kavramlar

**Dijital Görüntü Matrisi:**

$$
I(x,y) \in \mathbb{R}^{M \times N \times C}
$$

Burada:
- $M$ : Yükseklik (satır sayısı)
- $N$ : Genişlik (sütun sayısı)  
- $C$ : Kanal sayısı (Gri=1, RGB=3)

---

## 2. Örnekleme (Sampling)

**Nyquist-Shannon Örnekleme Teoremi:**

$$
f_s \geq 2 \cdot f_{max}
$$

**Yeniden Örnekleme (Downsampling):**

$$
I_{down}(x,y) = I(x \cdot k, y \cdot k)
$$

Burada $k$ örnekleme faktörüdür.

**Piksel Sayısı:**

$$
N_{pixels} = M \times N = \frac{M_{orig}}{k} \times \frac{N_{orig}}{k}
$$

---

## 3. Kuantalama (Quantization)

**Bit Derinliği ve Seviye Sayısı:**

$$
L = 2^b
$$

Burada:
- $b$ : Bit sayısı (1, 2, 4, 8, ...)
- $L$ : Gri seviye sayısı

**Kuantalama Formülü:**

$$
Q(I) = \left\lfloor \frac{I}{step} \right\rfloor \times step
$$

$$
step = \frac{256}{L} = \frac{256}{2^b}
$$

**Kuantalama Hatası:**

$$
e_q = I - Q(I)
$$

**Ortalama Kare Hata (MSE):**

$$
MSE = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} [I(x,y) - Q(I(x,y))]^2
$$

---

## 4. Renk Uzayları

### RGB (Red, Green, Blue)

$$
\vec{p} = \begin{bmatrix} R \\ G \\ B \end{bmatrix}, \quad R,G,B \in [0, 255]
$$

### Grayscale (Gri Tonlama)

**Luminosity Yöntemi (ITU-R BT.601):**

$$
Y = 0.299 \cdot R + 0.587 \cdot G + 0.114 \cdot B
$$

**Ortalama Yöntemi:**

$$
Y = \frac{R + G + B}{3}
$$

### HSV (Hue, Saturation, Value)

**RGB → HSV Dönüşümü:**

$$
V = \max(R, G, B)
$$

$$
S = \begin{cases} 0 & \text{if } V = 0 \\ \frac{V - \min(R,G,B)}{V} & \text{otherwise} \end{cases}
$$

$$
H = \begin{cases} 
0 & \text{if } S = 0 \\
60° \times \frac{G-B}{V-min} & \text{if } V = R \\
60° \times (2 + \frac{B-R}{V-min}) & \text{if } V = G \\
60° \times (4 + \frac{R-G}{V-min}) & \text{if } V = B
\end{cases}
$$

### YCbCr (Luminance, Chrominance)

$$
\begin{bmatrix} Y \\ Cb \\ Cr \end{bmatrix} = 
\begin{bmatrix} 0.299 & 0.587 & 0.114 \\ -0.169 & -0.331 & 0.500 \\ 0.500 & -0.419 & -0.081 \end{bmatrix}
\begin{bmatrix} R \\ G \\ B \end{bmatrix} +
\begin{bmatrix} 0 \\ 128 \\ 128 \end{bmatrix}
$$

---

## 13. Emboss (Kabartma) Efekti

Emboss efekti, konvolüsyon çekirdeği (kernel) kullanılarak uygulanır:

$$
K_{emboss} = \begin{bmatrix} -2 & -1 & 0 \\ -1 & 1 & 1 \\ 0 & 1 & 2 \end{bmatrix}
$$

**Konvolüsyon işlemi:**

$$
G(x,y) = \sum_{i=-1}^{1} \sum_{j=-1}^{1} K(i,j) \cdot I(x+i, y+j)
$$

---

## 14. Fourier Dönüşümü (FFT)

**2D Ayrık Fourier Dönüşümü:**

$$
F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) \cdot e^{-j2\pi(\frac{ux}{M} + \frac{vy}{N})}
$$

**Ters Fourier Dönüşümü:**

$$
f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) \cdot e^{j2\pi(\frac{ux}{M} + \frac{vy}{N})}
$$

**Büyüklük Spektrumu:**

$$
|F(u,v)| = \sqrt{R(u,v)^2 + I(u,v)^2}
$$

---

## 15. Hough Dönüşümü

### Çizgi Tespiti (Polar Form)

$$
\rho = x \cos\theta + y \sin\theta
$$

Burada:
- $\rho$ : Orijinden çizgiye dik uzaklık
- $\theta$ : Dik doğrunun x ekseniyle yaptığı açı
- $(x, y)$ : Görüntüdeki kenar noktası

### Daire Tespiti

$$
(x - a)^2 + (y - b)^2 = r^2
$$

Burada:
- $(a, b)$ : Dairenin merkez koordinatları
- $r$ : Dairenin yarıçapı

---

## Genel Konvolüsyon Formülü

$$
(I * K)(x,y) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} I(x-i, y-j) \cdot K(i,j)
$$

---

## Sobel Kenar Tespiti (Edge Detection)

**Sobel X (Yatay Gradyan):**

$$
G_x = \begin{bmatrix} -1 & 0 & +1 \\ -2 & 0 & +2 \\ -1 & 0 & +1 \end{bmatrix} * I
$$

**Sobel Y (Dikey Gradyan):**

$$
G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ +1 & +2 & +1 \end{bmatrix} * I
$$

**Gradyan Büyüklüğü:**

$$
G = \sqrt{G_x^2 + G_y^2}
$$

**Gradyan Yönü:**

$$
\theta = \arctan\left(\frac{G_y}{G_x}\right)
$$

---

## Gaussian Blur

**2D Gaussian Fonksiyonu:**

$$
G(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
$$

---

## Histogram Eşitleme

$$
s_k = (L-1) \sum_{j=0}^{k} p_r(r_j) = (L-1) \sum_{j=0}^{k} \frac{n_j}{MN}
$$

Burada:
- $L$ : Gri seviye sayısı (genellikle 256)
- $n_j$ : $j$ gri seviyesine sahip piksel sayısı
- $MN$ : Toplam piksel sayısı

---

## Threshold (Eşikleme)

**Global Threshold:**

$$
g(x,y) = \begin{cases} 255 & \text{if } f(x,y) > T \\ 0 & \text{otherwise} \end{cases}
$$

**Otsu Threshold (Sınıflar arası varyansı maksimize et):**

$$
\sigma_B^2(t) = \omega_0(t)\omega_1(t)[\mu_0(t) - \mu_1(t)]^2
$$

$$
t^* = \arg\max_{t} \sigma_B^2(t)
$$
