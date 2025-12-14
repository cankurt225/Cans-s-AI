import joblib
import os

# Model yolunu bul
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'api', 'knn_model.joblib')

print(f"Model yolu: {MODEL_PATH}")
print(f"Model var mı: {os.path.exists(MODEL_PATH)}")

if os.path.exists(MODEL_PATH):
    # Modeli yükle
    model = joblib.load(MODEL_PATH)
    
    print("\n[OK] Model yuklendi!")
    print(f"   Model tipi: {type(model)}")
    print(f"   Model sinifi: {model.__class__.__name__}")
    
    # Model metodlarını kontrol et
    print("\n[INFO] Model metodlari:")
    methods = [m for m in dir(model) if not m.startswith('_')]
    for method in methods[:20]:  # İlk 20 metodu göster
        print(f"   - {method}")
    
    # Predict var mı?
    has_predict = hasattr(model, 'predict')
    has_kneighbors = hasattr(model, 'kneighbors')
    
    print("\n[CHECK] Kontroller:")
    print(f"   predict() var mi: {has_predict}")
    print(f"   kneighbors() var mi: {has_kneighbors}")
    
    if not has_predict:
        print("\n[ERROR] SORUN: Bu model 'predict()' metoduna sahip degil!")
        print("   Model muhtemelen NearestNeighbors (unsupervised)")
        print("   KNeighborsClassifier veya KNeighborsRegressor kullanmalisiniz!")
else:
    print("[ERROR] Model dosyasi bulunamadi!")
