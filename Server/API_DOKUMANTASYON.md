# Prediction API'leri - Kullanım Kılavuzu

## 📍 Mevcut Endpoint'ler

### 1. **POST /api/predict/** (İlk Tahmin API)
Emlak verileri için KNN modeliyle tahmin yapar.

**Input Özellikleri (18 adet):**
- Furnished, University, Playground, Has_School
- Town_center, E_5, Sound_insulation, Security
- Gym, Price, m2_Net, Number_of_rooms
- Building_Age, Heating, Thermal_Insulation
- Hospital, The_health_clinic, Amusement_center

**Örnek İstek:**
```json
POST http://localhost:8000/api/predict/
{
  "Furnished": "1",
  "University": "0.5",
  "Playground": "0.3",
  ...
}
```

**Örnek Yanıt:**
```json
{
  "success": true,
  "prediction": 1,
  "probabilities": [0.3, 0.7],
  "input_features": {...}
}
```

---

### 2. **POST /api/predict2/** (İkinci Tahmin API) ⭐ YENİ
İkinci bir model için tahmin endpoint'i.

**Durum:** 🚧 Henüz özelleştirilmedi
**Yapılması Gerekenler:**
1. `Prediction2InputSerializer` içindeki feature'ları tanımlayın
2. Model dosyasını yükleyin (varsa)
3. Tahmin mantığını ekleyin

**Şu anda Örnek Yanıt:**
```json
{
  "success": true,
  "prediction": 1,
  "message": "Predict2 endpoint - Henüz model entegre edilmedi",
  "input_data": {...}
}
```

---

## 🔧 Predict2'yi Özelleştirmek İçin

### Adım 1: Serializer'ı Düzenle
`api/views.py` dosyasında `Prediction2InputSerializer` sınıfını düzenleyin:

```python
class Prediction2InputSerializer(serializers.Serializer):
    """İkinci tahmin API'si için input serializer"""
    # Kendi feature'larınızı ekleyin
    age = serializers.FloatField()
    income = serializers.FloatField()
    score = serializers.FloatField()
    # ...
```

### Adım 2: Model Yükle (Eğer varsa)
`api/views.py` dosyasının başında:

```python
# Model 2'yi yükle
MODEL2_PATH = os.path.join(BASE_DIR, 'model2.joblib')
try:
    model2 = joblib.load(MODEL2_PATH)
    print_debug(f"[OK] Model 2 yuklendi: {MODEL2_PATH}")
except Exception as e:
    model2 = None
    print_debug(f"[ERROR] Model 2 yuklenemedi: {e}")
```

### Adım 3: Tahmin Mantığını Ekle
`predict2` fonksiyonunda TODO kısmını doldurun:

```python
# Model kontrolü
if model2 is None:
    return Response(
        {'error': 'Model 2 yüklenemedi'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

# Feature'ları hazırla
data = serializer.validated_data
features = [data['age'], data['income'], data['score'], ...]
features_array = np.array([features])

# Tahmin yap
prediction = model2.predict(features_array)

response_data = {
    'success': True,
    'prediction': int(prediction[0]),
    'input_data': data
}
```

---

## 🧪 Test Etme

### Predict2'yi Test Et:
```bash
curl -X POST http://localhost:8000/api/predict2/ \
  -H "Content-Type: application/json" \
  -d '{"feature1": 1.0, "feature2": 2.0, "feature3": 3.0}'
```

Terminal'de şunu göreceksiniz:
```
🟢 PREDICT2 API ÇAĞRILDI
📦 Request Body: {"feature1": 1.0, ...}
✅ Validasyon başarılı
✅ Başarılı - Yanıt gönderiliyor
```

---

## 📝 Notlar

- Her iki endpoint de CSRF korumasından muaf (`@csrf_exempt`)
- CORS ayarları tüm kaynaklara açık
- Tüm loglar `print_debug()` ile terminale yazılır
- Hata durumlarında detaylı traceback gösterilir
