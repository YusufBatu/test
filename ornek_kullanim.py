#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UTKFace Basit Kullanım Örneği

Bu script, UTKFace veri setini kullanmak için basit bir örnek gösterir.
Bağımsız olarak çalıştırılabilir ve temel işlevleri gösterir.
"""

# Basit kullanım örneği - Dış kütüphane gerektirmez
def parse_utkface_filename_simple(filename):
    """
    UTKFace dosya isminden bilgi çıkarır - Basit versiyon
    """
    try:
        # Uzantıyı kaldır
        name = filename.replace('.jpg', '').replace('.jpeg', '').replace('.png', '')
        parts = name.split('_')
        
        age = int(parts[0])
        gender = int(parts[1])
        race = int(parts[2])
        
        # Türkçe etiketler
        gender_tr = 'Kadın' if gender == 1 else 'Erkek'
        
        race_dict = {
            0: 'Beyaz',
            1: 'Siyah', 
            2: 'Asyalı',
            3: 'Hint',
            4: 'Diğer'
        }
        race_tr = race_dict.get(race, 'Bilinmeyen')
        
        return {
            'filename': filename,
            'age': age,
            'gender': gender_tr,
            'race': race_tr,
            'success': True
        }
    except:
        return {
            'filename': filename,
            'error': 'Parse edilemedi',
            'success': False
        }


def main():
    """
    Örnek kullanım
    """
    print("=" * 60)
    print("UTKFace Dosya Adı Parse Örneği")
    print("=" * 60)
    print()
    
    # Örnek dosya adları
    test_files = [
        "39_1_0_20170116174525125.jpg",
        "25_0_2_20170117003344913.jpg",
        "62_1_3_20170109150557335.jpg",
        "18_0_1_20170116192950904.jpg",
        "45_1_4_20170109174534484.jpg"
    ]
    
    print("📝 Örnek Dosya Adları Parse Ediliyor...\n")
    
    for filename in test_files:
        result = parse_utkface_filename_simple(filename)
        
        if result['success']:
            print(f"Dosya: {result['filename']}")
            print(f"  └─ Yaş: {result['age']}")
            print(f"  └─ Cinsiyet: {result['gender']}")
            print(f"  └─ Irk: {result['race']}")
            print()
        else:
            print(f"❌ Hata: {result['filename']} - {result['error']}")
            print()
    
    print("=" * 60)
    print("📊 İstatistikler")
    print("=" * 60)
    
    # Basit istatistik hesaplama
    ages = []
    genders = {'Erkek': 0, 'Kadın': 0}
    races = {}
    
    for filename in test_files:
        result = parse_utkface_filename_simple(filename)
        if result['success']:
            ages.append(result['age'])
            genders[result['gender']] += 1
            races[result['race']] = races.get(result['race'], 0) + 1
    
    if ages:
        print(f"\nYaş İstatistikleri:")
        print(f"  └─ Minimum: {min(ages)}")
        print(f"  └─ Maximum: {max(ages)}")
        print(f"  └─ Ortalama: {sum(ages) / len(ages):.1f}")
        
        print(f"\nCinsiyet Dağılımı:")
        for gender, count in genders.items():
            print(f"  └─ {gender}: {count}")
        
        print(f"\nIrk Dağılımı:")
        for race, count in sorted(races.items()):
            print(f"  └─ {race}: {count}")
    
    print("\n" + "=" * 60)
    print("✅ Test tamamlandı!")
    print("=" * 60)
    print()
    print("📚 Daha fazla özellik için:")
    print("  • utkface_helper.py - Gelişmiş fonksiyonlar")
    print("  • UTKFace_Google_Colab_Kullanimi.ipynb - Tam rehber")
    print()


if __name__ == "__main__":
    main()
