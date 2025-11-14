# UTKFace Cropped Images - Google Colab Kullanım Rehberi

Bu repository, UTKFace veri setindeki kırpılmış (cropped) yüz görsellerini Google Colab üzerinde nasıl kullanacağınızı gösteren kapsamlı bir rehber içerir.

## 📋 İçindekiler

- UTKFace veri seti hakkında bilgi
- Google Colab'da veri setini indirme ve yükleme yöntemleri
- Dosya isimlerinden metadata (yaş, cinsiyet, ırk) çıkarma
- Veri setini keşfetme ve görselleştirme
- Görsel ön işleme teknikleri
- Batch halinde veri yükleme
- TensorFlow/Keras ile kullanım
- PyTorch ile kullanım

## 🚀 Hızlı Başlangıç

### Google Colab'da Çalıştırma

1. **Notebook'u Aç**: `UTKFace_Google_Colab_Kullanimi.ipynb` dosyasını Google Colab'da açın
   - Google Colab'a gidin: https://colab.research.google.com/
   - `File` → `Upload notebook` seçeneğini kullanarak notebook'u yükleyin
   - Veya GitHub'dan direkt açın

2. **Gerekli Kütüphaneleri Yükleyin**: Notebook'taki ilk hücreyi çalıştırın

3. **Veri Setini İndirin**: Notebook'ta üç farklı indirme yöntemi sunulmaktadır:
   - **Kaggle API** (Önerilen)
   - **Google Drive**
   - **Manuel Yükleme**

4. **Veri Keşfine Başlayın**: Notebook'taki adımları takip ederek veri setini keşfedin

## 📊 UTKFace Veri Seti Hakkında

UTKFace, 20.000'den fazla yüz görselini içeren büyük ölçekli bir veri setidir. Her görsel yaş, cinsiyet ve etnik köken bilgilerini içerir.

### Dosya İsimlendirme Formatı

```
[yaş]_[cinsiyet]_[ırk]_[tarih&zaman].jpg
```

**Parametreler:**
- **Yaş**: 0-116 arası tam sayı
- **Cinsiyet**: 0 (Erkek), 1 (Kadın)
- **Irk**: 0 (Beyaz), 1 (Siyah), 2 (Asyalı), 3 (Hint), 4 (Diğer)

**Örnek:** `39_1_0_20170116174525125.jpg`
- Yaş: 39
- Cinsiyet: Kadın (1)
- Irk: Beyaz (0)

## 🛠️ Özellikler

### Veri İndirme Yöntemleri

1. **Kaggle API**: En hızlı ve pratik yöntem
2. **Google Drive**: Veri setiniz zaten Drive'da mevcutsa
3. **Manuel Yükleme**: Yerel dosyalardan yükleme

### Veri İşleme Fonksiyonları

- ✅ Dosya isimlerinden otomatik metadata çıkarma
- ✅ Pandas DataFrame ile organize veri yönetimi
- ✅ Yaş, cinsiyet ve ırk bazlı filtreleme
- ✅ Görsel ön işleme ve normalizasyon
- ✅ Batch data generator
- ✅ Train/Validation/Test ayrımı

### Görselleştirme

- 📊 Yaş, cinsiyet ve ırk dağılım grafikleri
- 🖼️ Rastgele görsel görüntüleme
- 🔍 Filtrelenmiş görsel görüntüleme

### Deep Learning Framework Desteği

- 🔥 **TensorFlow/Keras**: ImageDataGenerator ile veri artırma
- 🔥 **PyTorch**: Custom Dataset ve DataLoader implementasyonu

## 📝 Kullanım Örnekleri

### Basit Görsel Yükleme

```python
import glob
from PIL import Image

# Tüm görselleri listele
image_paths = glob.glob('utkface_data/UTKFace/*.jpg')

# İlk görseli aç
img = Image.open(image_paths[0])
img.show()
```

### Metadata Çıkarma

```python
def parse_filename(filename):
    parts = filename.split('_')
    age = int(parts[0])
    gender = int(parts[1])  # 0: Erkek, 1: Kadın
    race = int(parts[2])    # 0-4 arası
    return age, gender, race

filename = "39_1_0_20170116174525125.jpg"
age, gender, race = parse_filename(filename)
print(f"Yaş: {age}, Cinsiyet: {gender}, Irk: {race}")
```

### Filtreleme

```python
import pandas as pd

# DataFrame'den filtreleme
filtered = df[(df['age'] >= 20) & (df['age'] <= 30) & (df['gender'] == 'Kadın')]
print(f"20-30 yaş arası kadın sayısı: {len(filtered)}")
```

## 🎓 Kullanım Senaryoları

Bu veri seti ile yapabileceğiniz projeler:

1. **Yaş Tahmini**: Yüz görselinden yaş tahmin modeli
2. **Cinsiyet Sınıflandırması**: Erkek/Kadın sınıflandırma
3. **Irk Tanıma**: Etnik köken sınıflandırma
4. **Multi-task Learning**: Aynı anda birden fazla özellik tahmini
5. **Face Recognition**: Yüz tanıma sistemleri
6. **Transfer Learning**: Önceden eğitilmiş modeller ile fine-tuning

## 📦 Gereksinimler

Notebook'ta kullanılan temel kütüphaneler:

```
numpy
pandas
matplotlib
Pillow
tqdm
scikit-learn
```

Opsiyonel (Deep Learning için):
```
tensorflow
torch
torchvision
```

Google Colab'da çoğu kütüphane zaten yüklüdür.

## 🔗 Faydalı Linkler

- [UTKFace Resmi Website](https://susanqq.github.io/UTKFace/)
- [Kaggle UTKFace Dataset](https://www.kaggle.com/datasets/jangedoo/utkface-new)
- [Google Colab](https://colab.research.google.com/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [PyTorch Documentation](https://pytorch.org/)

## 💡 İpuçları

1. **GPU Kullanımı**: Google Colab'da GPU kullanmak için `Runtime` → `Change runtime type` → `GPU` seçin
2. **Veri Kalıcılığı**: Google Drive'ı mount ederek verilerinizi kalıcı hale getirin
3. **Bellek Yönetimi**: Büyük veri setleri için batch processing kullanın
4. **Data Augmentation**: Model performansını artırmak için veri artırma teknikleri kullanın

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz:

1. Repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje eğitim amaçlıdır. UTKFace veri seti için orijinal lisans koşullarına uyunuz.

## 📧 İletişim

Sorularınız veya önerileriniz için issue açabilirsiniz.

---

**Not**: Bu notebook tamamen Türkçe olarak hazırlanmıştır ve Google Colab'da sorunsuz çalışacak şekilde optimize edilmiştir.
