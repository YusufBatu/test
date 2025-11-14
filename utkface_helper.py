#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UTKFace Dataset Helper - Yardımcı Fonksiyonlar

Bu script, UTKFace veri setini kullanmak için temel yardımcı fonksiyonlar içerir.
Google Colab veya yerel Python ortamında kullanılabilir.
"""

import os
import glob
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


def parse_utkface_filename(filename):
    """
    UTKFace dosya isminden yaş, cinsiyet ve ırk bilgilerini çıkarır.
    
    Format: [yaş]_[cinsiyet]_[ırk]_[tarih].jpg
    
    Args:
        filename (str): Dosya adı (örn: "39_1_0_20170116174525125.jpg")
    
    Returns:
        dict: Yaş, cinsiyet ve ırk bilgilerini içeren sözlük
              None döner eğer parse edilemezse
    
    Örnek:
        >>> parse_utkface_filename("39_1_0_20170116174525125.jpg")
        {'age': 39, 'gender': 1, 'gender_label': 'Kadın', 
         'race': 0, 'race_label': 'Beyaz'}
    """
    try:
        # Dosya uzantısını kaldır ve parçalara ayır
        parts = os.path.splitext(filename)[0].split('_')
        
        age = int(parts[0])
        gender = int(parts[1])
        race = int(parts[2])
        
        # Etiketleri anlamlı hale getir
        gender_label = 'Kadın' if gender == 1 else 'Erkek'
        
        race_labels = {
            0: 'Beyaz',
            1: 'Siyah',
            2: 'Asyalı',
            3: 'Hint',
            4: 'Diğer'
        }
        race_label = race_labels.get(race, 'Bilinmeyen')
        
        return {
            'age': age,
            'gender': gender,
            'gender_label': gender_label,
            'race': race,
            'race_label': race_label
        }
    except (ValueError, IndexError) as e:
        print(f"Hata: '{filename}' dosya adı parse edilemedi - {e}")
        return None


def load_utkface_dataset(data_dir, extensions=['*.jpg', '*.jpeg', '*.png']):
    """
    UTKFace veri setini yükler ve DataFrame oluşturur.
    
    Args:
        data_dir (str): Veri setinin bulunduğu klasör yolu
        extensions (list): Görsel dosya uzantıları
    
    Returns:
        pd.DataFrame: Tüm görseller ve metadata bilgilerini içeren DataFrame
    
    Örnek:
        >>> df = load_utkface_dataset('utkface_data/UTKFace/')
        >>> print(f"Toplam {len(df)} görsel yüklendi")
    """
    print(f"Veri seti yükleniyor: {data_dir}")
    
    # Tüm görsel dosyalarını bul
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(data_dir, ext)))
    
    print(f"Toplam {len(image_paths)} dosya bulundu")
    
    # Her dosya için metadata çıkar
    data_list = []
    skipped = 0
    
    for img_path in image_paths:
        filename = os.path.basename(img_path)
        metadata = parse_utkface_filename(filename)
        
        if metadata:
            data_list.append({
                'filename': filename,
                'filepath': img_path,
                'age': metadata['age'],
                'gender': metadata['gender_label'],
                'gender_code': metadata['gender'],
                'race': metadata['race_label'],
                'race_code': metadata['race']
            })
        else:
            skipped += 1
    
    if skipped > 0:
        print(f"Uyarı: {skipped} dosya parse edilemedi ve atlandı")
    
    # DataFrame oluştur
    df = pd.DataFrame(data_list)
    print(f"DataFrame oluşturuldu: {len(df)} kayıt")
    
    return df


def display_sample_images(df, n=9, figsize=(15, 15), seed=None):
    """
    Rastgele örnek görselleri görüntüler.
    
    Args:
        df (pd.DataFrame): Görsel verilerini içeren DataFrame
        n (int): Görüntülenecek görsel sayısı
        figsize (tuple): Figure boyutu
        seed (int): Rastgelelik için seed değeri
    
    Örnek:
        >>> display_sample_images(df, n=9)
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Rastgele örnekler seç
    if len(df) < n:
        print(f"Uyarı: Sadece {len(df)} görsel mevcut")
        n = len(df)
    
    samples = df.sample(n=n)
    
    # Grid hesapla
    rows = int(np.ceil(np.sqrt(n)))
    cols = int(np.ceil(n / rows))
    
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    if n == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    
    for idx, (_, row) in enumerate(samples.iterrows()):
        if idx >= n:
            break
        
        # Görseli yükle ve göster
        try:
            img = Image.open(row['filepath'])
            axes[idx].imshow(img)
            axes[idx].axis('off')
            axes[idx].set_title(
                f"Yaş: {row['age']}\n{row['gender']}, {row['race']}",
                fontsize=10
            )
        except Exception as e:
            axes[idx].text(0.5, 0.5, f'Hata:\n{str(e)}',
                          ha='center', va='center')
            axes[idx].axis('off')
    
    # Kullanılmayan eksenleri gizle
    for idx in range(n, len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    plt.show()


def get_dataset_statistics(df):
    """
    Veri seti istatistiklerini hesaplar ve gösterir.
    
    Args:
        df (pd.DataFrame): Görsel verilerini içeren DataFrame
    
    Returns:
        dict: İstatistik bilgilerini içeren sözlük
    
    Örnek:
        >>> stats = get_dataset_statistics(df)
        >>> print(stats)
    """
    stats = {
        'total_images': len(df),
        'age_range': (df['age'].min(), df['age'].max()),
        'age_mean': df['age'].mean(),
        'age_median': df['age'].median(),
        'gender_distribution': df['gender'].value_counts().to_dict(),
        'race_distribution': df['race'].value_counts().to_dict()
    }
    
    # İstatistikleri yazdır
    print("=" * 50)
    print("UTKFace VERİ SETİ İSTATİSTİKLERİ")
    print("=" * 50)
    print(f"\nToplam Görsel Sayısı: {stats['total_images']}")
    print(f"\nYaş İstatistikleri:")
    print(f"  - Aralık: {stats['age_range'][0]} - {stats['age_range'][1]}")
    print(f"  - Ortalama: {stats['age_mean']:.2f}")
    print(f"  - Medyan: {stats['age_median']:.2f}")
    print(f"\nCinsiyet Dağılımı:")
    for gender, count in stats['gender_distribution'].items():
        percentage = (count / stats['total_images']) * 100
        print(f"  - {gender}: {count} (%{percentage:.1f})")
    print(f"\nIrk Dağılımı:")
    for race, count in stats['race_distribution'].items():
        percentage = (count / stats['total_images']) * 100
        print(f"  - {race}: {count} (%{percentage:.1f})")
    print("=" * 50)
    
    return stats


def plot_distributions(df, figsize=(15, 5)):
    """
    Yaş, cinsiyet ve ırk dağılımlarını görselleştirir.
    
    Args:
        df (pd.DataFrame): Görsel verilerini içeren DataFrame
        figsize (tuple): Figure boyutu
    
    Örnek:
        >>> plot_distributions(df)
    """
    fig, axes = plt.subplots(1, 3, figsize=figsize)
    
    # Yaş dağılımı
    df['age'].hist(bins=50, ax=axes[0], edgecolor='black', color='skyblue')
    axes[0].set_title('Yaş Dağılımı', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Yaş')
    axes[0].set_ylabel('Frekans')
    axes[0].grid(alpha=0.3)
    
    # Cinsiyet dağılımı
    gender_counts = df['gender'].value_counts()
    axes[1].bar(gender_counts.index, gender_counts.values, color=['#FF6B6B', '#4ECDC4'])
    axes[1].set_title('Cinsiyet Dağılımı', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Cinsiyet')
    axes[1].set_ylabel('Sayı')
    axes[1].grid(alpha=0.3, axis='y')
    
    # Irk dağılımı
    race_counts = df['race'].value_counts()
    axes[2].bar(race_counts.index, race_counts.values, 
                color=['#95E1D3', '#F38181', '#AA96DA', '#FCBAD3', '#FFFFD2'])
    axes[2].set_title('Irk Dağılımı', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Irk')
    axes[2].set_ylabel('Sayı')
    axes[2].tick_params(axis='x', rotation=45)
    axes[2].grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()


def filter_dataset(df, age_min=None, age_max=None, gender=None, race=None):
    """
    Veri setini belirtilen kriterlere göre filtreler.
    
    Args:
        df (pd.DataFrame): Görsel verilerini içeren DataFrame
        age_min (int): Minimum yaş
        age_max (int): Maximum yaş
        gender (str): Cinsiyet ('Erkek' veya 'Kadın')
        race (str): Irk ('Beyaz', 'Siyah', 'Asyalı', 'Hint', 'Diğer')
    
    Returns:
        pd.DataFrame: Filtrelenmiş DataFrame
    
    Örnek:
        >>> # 20-30 yaş arası kadınları filtrele
        >>> filtered = filter_dataset(df, age_min=20, age_max=30, gender='Kadın')
        >>> print(f"Filtrelenmiş: {len(filtered)} görsel")
    """
    filtered = df.copy()
    
    if age_min is not None:
        filtered = filtered[filtered['age'] >= age_min]
    
    if age_max is not None:
        filtered = filtered[filtered['age'] <= age_max]
    
    if gender is not None:
        filtered = filtered[filtered['gender'] == gender]
    
    if race is not None:
        filtered = filtered[filtered['race'] == race]
    
    print(f"Filtreleme sonucu: {len(filtered)} görsel (orijinal: {len(df)})")
    
    return filtered


def load_and_preprocess_image(filepath, target_size=(224, 224), normalize=True):
    """
    Görseli yükler ve ön işleme yapar.
    
    Args:
        filepath (str): Görsel dosya yolu
        target_size (tuple): Hedef boyut (genişlik, yükseklik)
        normalize (bool): Piksel değerlerini 0-1 arasına normalize et
    
    Returns:
        np.ndarray: İşlenmiş görsel
    
    Örnek:
        >>> img = load_and_preprocess_image('path/to/image.jpg')
        >>> print(img.shape)  # (224, 224, 3)
    """
    # Görseli yükle
    img = Image.open(filepath).convert('RGB')
    
    # Boyutlandır
    img = img.resize(target_size)
    
    # Numpy array'e çevir
    img_array = np.array(img)
    
    # Normalize et
    if normalize:
        img_array = img_array.astype('float32') / 255.0
    
    return img_array


# Test fonksiyonu
def main():
    """
    Ana test fonksiyonu - Temel kullanım örneği
    """
    print("UTKFace Dataset Helper - Test")
    print("-" * 50)
    
    # Örnek dosya adı parse etme
    test_filename = "39_1_0_20170116174525125.jpg"
    print(f"\nTest dosyası: {test_filename}")
    metadata = parse_utkface_filename(test_filename)
    print(f"Metadata: {metadata}")
    
    print("\n" + "-" * 50)
    print("Veri setini yüklemek için:")
    print("df = load_utkface_dataset('utkface_data/UTKFace/')")
    print("\nDaha fazla örnek için notebook'a bakınız:")
    print("UTKFace_Google_Colab_Kullanimi.ipynb")


if __name__ == "__main__":
    main()
