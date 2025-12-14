# Random Forest Predict2 API - Kullanım Kılavuzu

## 🌳 Endpoint Bilgileri

**URL:** `POST http://localhost:8000/api/predict2/`
**Model:** Random Forest
**Amaç:** Emlak tahmini (Random Forest algoritması ile)

---

## 📋 Input Özellikleri (11 adet)

| Field Adı (İngilizce) | Field Adı (Türkçe) | Tip | Açıklama |
|----------------------|-------------------|-----|----------|
| `District` | İlçe | String | İlçe adı (categorical) |
| `Neighborhood` | Mahalle | String | Mahalle adı (categorical) |
| `Price` | Fiyat | Float | Emlak fiyatı |
| `m2_Gross` | Brüt m² | Float | Brüt metrekare |
| `m2_Net` | Net m² | Float | Net metrekare |
| `Number_of_rooms` | Oda Sayısı | Float | Oda sayısı |
| `Building_Age` | Bina Yaşı | Float | Bina yaşı |
| `Floor_location` | Bulunduğu Kat | Float | Kat bilgisi |
| `Heating` | Isıtma Tipi | Float | Isıtma sistemi (encoded) |
| `Sea` | Deniz Manzarası | Float | Deniz manzarası var mı (0/1) |
| `Throat` | Boğaz Manzarası | Float | Boğaz manzarası var mı (0/1) |

---

## 🧪 Örnek İstekler

### Örnek 1: İngilizce Field İsimleri
```json
POST http://localhost:8000/api/predict2/
Content-Type: application/json

{
  "District": "Beşiktaş",
  "Neighborhood": "Levent",
  "Price": 5000000,
  "m2_Gross": 150,
  "m2_Net": 130,
  "Number_of_rooms": 3,
  "Building_Age": 5,
  "Floor_location": 8,
  "Heating": 1.0,
  "Sea": 1,
  "Throat": 0
}
```

### Örnek 2: Türkçe Field İsimleri (Otomatik Dönüşüm)
```json
POST http://localhost:8000/api/predict2/
Content-Type: application/json

{
  "İlçe": "Kadıköy",
  "Mahalle": "Moda",
  "Fiyat": 3500000,
  "Brüt m²": 120,
  "Net m²": 100,
  "Oda Sayısı": 2,
  "Bina Yaşı": 10,
  "Bulunduğu Kat": 5,
  "Isıtma Tipi": 1.5,
  "Deniz Manzarası": 1,
  "Boğaz Manzarası": 1
}
```

### Örnek 3: Karışık (Mix)
```json
{
  "District": "Sarıyer",
  "Mahalle": "İstinye",
  "Price": 10000000,
  "m² (Gross)": 250,
  "m² (Net)": 220,
  "Number of rooms": 4,
  "Building Age": 2,
  "Floor location": 12,
  "Heating": 2.0,
  "Sea": 1,
  "Throat": 1
}
```

---

## 📤 Örnek Yanıt

```json
{
  "success": true,
  "prediction": 1,
  "probabilities": [0.23, 0.77],
  "input_features": {
    "District": "Beşiktaş",
    "Neighborhood": "Levent",
    "Price": 5000000.0,
    "m2_Gross": 150.0,
    "m2_Net": 130.0,
    "Number_of_rooms": 3.0,
    "Building_Age": 5.0,
    "Floor_location": 8.0,
    "Heating": 1.0,
    "Sea": 1.0,
    "Throat": 0.0
  },
  "model_type": "RandomForest"
}
```

---

## 🔧 Terminal Logları

API çağrıldığında terminalde şu logları göreceksiniz:

```
================================================================================
🟢 PREDICT2 API (Random Forest) ÇAĞRILDI - 2025-12-14 07:14:00
================================================================================
📍 Method: POST
📍 Path: /api/predict2/
📍 Client IP: 127.0.0.1
📦 Request Body:
{"District":"Beşiktaş","Neighborhood":"Levent",... }
✅ Random Forest modeli hazır
🔍 Validasyon başlatılıyor...
📥 Gelen veri (orijinal): ['District', 'Neighborhood', ...]
📥 Gelen veri (transform edilmiş): ['District', 'Neighborhood', ...]
✅ Validasyon başarılı
📊 Gelen features:
   District: Beşiktaş
   Neighborhood: Levent
   Price: 5000000.0
   ...
📊 Feature array shape: (1, 11)
📊 Feature values: ['Beşiktaş', 'Levent', 5000000.0, ...]
🎯 Tahmin: 1
📈 Olasılıklar: [0.23, 0.77]
✅ Başarılı - Yanıt gönderiliyor
================================================================================
```

---

## ⚠️ Önemli Notlar

### 1. **Categorical Encoding**
- `District` ve `Neighborhood` field'ları string olarak gelir
- Model bu string değerleri handle edebiliyorsa sorun yok
- Değilse, modelin eğitildiği **LabelEncoder** veya **OneHotEncoder** ile encode edilmeli!

### 2. **Field Mapping**
API hem Türkçe hem İngilizce field isimlerini destekler:
- Türkçe → İngilizce otomatik dönüşüm
- Boşluklu isimler → Alt çizgili isimler

Mapping listesi:
```python
'İlçe' → 'District'
'Mahalle' → 'Neighborhood'
'm² (Gross)' → 'm2_Gross'
'Number of rooms' → 'Number_of_rooms'
...
```

### 3. **Model Dosyası**
Model dosyası şu konumda olmalı:
```
Server/api/random_forest_model.joblib
```

Yoksa şu hatayı alırsınız:
```
❌ [ERROR] Random Forest modeli yüklenemedi
```

---

## 🧪 cURL ile Test

```bash
curl -X POST http://localhost:8000/api/predict2/ \
  -H "Content-Type: application/json" \
  -d '{
    "District": "Beşiktaş",
    "Neighborhood": "Levent",
    "Price": 5000000,
    "m2_Gross": 150,
    "m2_Net": 130,
    "Number_of_rooms": 3,
    "Building_Age": 5,
    "Floor_location": 8,
    "Heating": 1.0,
    "Sea": 1,
    "Throat": 0
  }'
```

---

## 🚀 Next Steps

1. **Model Dosyasını Ekle:** `random_forest_model.joblib` dosyasını `api/` klasörüne kopyalayın
2. **Categorical Encoding:** Eğer model categorical encoding bekyliyorsa, encoder'ları yükleyin
3. **Test Et:** Flutter'dan veya cURL ile test yapın
4. **İzle:** Terminal loglarını takip edin

Başarılar! 🎉
