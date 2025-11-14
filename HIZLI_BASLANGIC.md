# Hızlı Başlangıç Rehberi - UTKFace Google Colab

Bu rehber, UTKFace veri setini Google Colab'da kullanmaya hızlıca başlamanız için adım adım talimatlar içerir.

## 🚀 5 Dakikada Başlayın

### Adım 1: Google Colab'ı Açın
1. Tarayıcınızda https://colab.research.google.com/ adresine gidin
2. Google hesabınızla giriş yapın

### Adım 2: Notebook'u Yükleyin
1. `File` → `Upload notebook` menüsünü seçin
2. `UTKFace_Google_Colab_Kullanimi.ipynb` dosyasını seçin ve yükleyin

**Alternatif:** GitHub'dan direkt açmak için:
1. `File` → `Open notebook` 
2. `GitHub` sekmesine gidin
3. Repository URL'sini girin: `YusufBatu/test`
4. `UTKFace_Google_Colab_Kullanimi.ipynb` dosyasını seçin

### Adım 3: Runtime'ı Ayarlayın (Opsiyonel ama Önerilen)
1. `Runtime` → `Change runtime type` menüsüne gidin
2. `Hardware accelerator` olarak `GPU` seçin
3. `Save` butonuna tıklayın

> **Neden GPU?** Büyük veri setleri ile çalışırken ve özellikle deep learning modelleri eğitirken GPU kullanımı işlemleri çok daha hızlandırır.

### Adım 4: İlk Hücreyi Çalıştırın
1. İlk kod hücresine tıklayın
2. `Shift + Enter` tuşlarına basın veya sol taraftaki ▶️ butonuna tıklayın
3. Kütüphanelerin yüklendiğini görün

```python
# Gerekli kütüphaneleri import edin
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
...
```

### Adım 5: Veri Setini İndirin

**Seçenek A - Kaggle'dan İndirme (Önerilen):**

1. Kaggle hesabı açın (https://www.kaggle.com/)
2. Account ayarlarından API token indirin (kaggle.json)
3. Notebook'ta ilgili hücreyi çalıştırın
4. Dosya yükleme penceresi açıldığında `kaggle.json` dosyanızı seçin
5. Veri seti otomatik indirilecek

```python
# Kaggle API kurulumu
!pip install -q kaggle

# Token yükle ve veri setini indir
# (Notebook'taki kodları çalıştırın)
```

**Seçenek B - Manuel Yükleme:**

1. UTKFace veri setini bilgisayarınıza indirin
2. ZIP dosyasını hazır bulundurun
3. Notebook'ta manuel yükleme hücresini çalıştırın
4. Dosya seçme penceresinden ZIP dosyanızı seçin

### Adım 6: Veriyi Keşfedin

Notebook'taki hücreleri sırayla çalıştırarak:

1. ✅ Veri setini görüntüleyin
2. ✅ İstatistikleri inceleyin
3. ✅ Grafikleri oluşturun
4. ✅ Rastgele görselleri görüntüleyin

```python
# Veri seti yükleme
df = load_utkface_dataset('utkface_data/UTKFace/')

# Temel istatistikler
print(df.describe())

# Görsel gösterme
display_images(df, n=9)
```

## 📖 Detaylı Kullanım

### Filtreleme Örneği

```python
# 20-30 yaş arası kadınları filtrele
filtered_df = df[(df['age'] >= 20) & 
                 (df['age'] <= 30) & 
                 (df['gender'] == 'Kadın')]

print(f"Filtrelenmiş: {len(filtered_df)} görsel")

# Filtrelenmiş görselleri göster
display_images(filtered_df, n=9)
```

### Tek Bir Görseli Yükleme

```python
from PIL import Image

# İlk görseli yükle
img_path = df.iloc[0]['filepath']
img = Image.open(img_path)
img.show()

# Bilgileri göster
print(f"Yaş: {df.iloc[0]['age']}")
print(f"Cinsiyet: {df.iloc[0]['gender']}")
print(f"Irk: {df.iloc[0]['race']}")
```

### Yaş Dağılımını Görüntüleme

```python
import matplotlib.pyplot as plt

# Yaş histogramı
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=50, edgecolor='black')
plt.title('UTKFace - Yaş Dağılımı')
plt.xlabel('Yaş')
plt.ylabel('Frekans')
plt.grid(alpha=0.3)
plt.show()
```

## 🎯 Sonraki Adımlar

Veri setini başarıyla yükledikten sonra:

### 1. Makine Öğrenmesi Modeli Eğitimi

```python
from sklearn.model_selection import train_test_split

# Veriyi ayır
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

print(f"Eğitim: {len(train_df)} görsel")
print(f"Test: {len(test_df)} görsel")
```

### 2. Deep Learning ile Yaş Tahmini

```python
import tensorflow as tf
from tensorflow import keras

# Model oluştur
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    # ... daha fazla layer
    keras.layers.Dense(1, activation='linear')  # Yaş tahmini için
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
```

### 3. Transfer Learning

```python
from tensorflow.keras.applications import ResNet50

# Önceden eğitilmiş model
base_model = ResNet50(weights='imagenet', 
                      include_top=False, 
                      input_shape=(224, 224, 3))

# Modelinizi oluşturun
# ...
```

## ❓ Sık Sorulan Sorular

### Veri seti ne kadar büyük?
UTKFace veri seti yaklaşık 20.000+ görsel içerir ve toplam boyutu ~500 MB'tır.

### Google Colab'da yeterli alan var mı?
Evet, Google Colab ücretsiz versiyonda ~108 GB disk alanı sunar.

### Session süresi dolunca ne olur?
Google Colab session'ları 12 saat sonra kapanır. Verilerinizi Google Drive'a kaydedin.

### GPU kullanmalı mıyım?
Sadece görselleştirme yapıyorsanız gerekmez ama model eğitimi için kesinlikle önerilir.

### Hata alırsam ne yapmalıyım?
1. Runtime'ı yeniden başlatın: `Runtime` → `Restart runtime`
2. Tüm hücreleri temizleyin: `Runtime` → `Restart and run all`
3. Google Drive bağlantısını kontrol edin
4. Dosya yollarının doğru olduğundan emin olun

## 💾 Verilerinizi Kaydetme

### Google Drive'a Kaydetme

```python
from google.colab import drive

# Drive'ı bağla
drive.mount('/content/drive')

# DataFrame'i kaydet
df.to_csv('/content/drive/MyDrive/utkface_data.csv', index=False)

# Model ağırlıklarını kaydet
model.save('/content/drive/MyDrive/utkface_model.h5')
```

### Yerel Bilgisayara İndirme

```python
from google.colab import files

# DataFrame'i indir
df.to_csv('utkface_data.csv', index=False)
files.download('utkface_data.csv')
```

## 🔗 Yararlı Kaynaklar

- 📚 [UTKFace Resmi Sayfa](https://susanqq.github.io/UTKFace/)
- 📊 [Kaggle Dataset](https://www.kaggle.com/datasets/jangedoo/utkface-new)
- 🎓 [Google Colab Kullanım Rehberi](https://colab.research.google.com/notebooks/intro.ipynb)
- 🔥 [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- 🐍 [Python Image Processing](https://pillow.readthedocs.io/)

## 📞 Destek

Sorunlarınız için:
1. Notebook içindeki dokümantasyonu kontrol edin
2. README.md dosyasını okuyun
3. GitHub'da issue açın
4. Kaggle discussion'larına bakın

---

**Başarılar! 🎉** 

Artık UTKFace veri setini Google Colab'da kullanmaya hazırsınız. Notebook'taki tüm hücreleri sırayla çalıştırarak adım adım ilerleyin.
