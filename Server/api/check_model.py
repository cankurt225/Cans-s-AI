"""
Random Forest modelinin feature names'ini kontrol et
"""
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RF_MODEL_PATH = os.path.join(BASE_DIR, 'random_forest_model.joblib')

# Model yükle
rf_model = joblib.load(RF_MODEL_PATH)

print("="*80)
print("RANDOM FOREST MODEL BİLGİLERİ")
print("="*80)
print(f"Model tipi: {type(rf_model)}")
print(f"Beklenen feature sayısı: {rf_model.n_features_in_}")

# Feature names varsa göster
if hasattr(rf_model, 'feature_names_in_'):
    print(f"\nFeature names sayısı: {len(rf_model.feature_names_in_)}")
    print("\nİlk 20 feature:")
    for i, name in enumerate(rf_model.feature_names_in_[:20]):
        print(f"  {i+1}. {name}")
    
    print("\n...")
    print("\nSon 20 feature:")
    for i, name in enumerate(rf_model.feature_names_in_[-20:]):
        print(f"  {len(rf_model.feature_names_in_)-20+i+1}. {name}")
    
    # District ve Neighborhood ile başlayan feature'ları say
    district_features = [f for f in rf_model.feature_names_in_ if f.startswith('District')]
    neighborhood_features = [f for f in rf_model.feature_names_in_ if f.startswith('Neighborhood')]
    
    print(f"\n'District' ile başlayan feature sayısı: {len(district_features)}")
    print(f"'Neighborhood' ile başlayan feature sayısı: {len(neighborhood_features)}")
    
    if district_features:
        print(f"\nİlk 10 District feature:")
        for f in district_features[:10]:
            print(f"  - {f}")
    
    if neighborhood_features:
        print(f"\nİlk 10 Neighborhood feature:")
        for f in neighborhood_features[:10]:
            print(f"  - {f}")
else:
    print("\nModel'de feature names bilgisi yok")

print("="*80)
