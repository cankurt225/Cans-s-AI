# -*- coding: utf-8 -*-
import re

# Dosyayı oku
with open(r'api\views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Emoji mapping - hepsini ASCII karakterlerle değiştir
emoji_replacements = {
    '🔵': '[PREDICT]',
    '🟢': '[PREDICT2]',
    '📍': '[INFO]',
    '📦': '[DATA]',
    '⚠️': '[WARNING]',
    '❌': '[ERROR]',
    '✅': '[OK]',
    '🔍': '[CHECK]',
    '📥': '[INPUT]',
    '📊': '[FEATURES]',
    '🎯': '[RESULT]',
    '📈': '[PROBA]',
    'ℹ️': '[INFO]',
    '✓': 'OK',
    '✗': 'ERROR',
    '⭐': '*',
    '🚀': '[START]',
    '📁': '[FILE]',
    '🌳': '[TREE]',
    '🎉': '!',
}

# Tüm emoji'leri değiştir
modified_content = content
for emoji, replacement in emoji_replacements.items():
    modified_content = modified_content.replace(emoji, replacement)

# Kalan tüm Unicode karakterleri de temizle (Türkçe karakterler hariç)
# Türkçe karakterler: ğ, ü, ş, ı, ö, ç, Ğ, Ü, Ş, İ, Ö, Ç
turkish_chars = 'ğüşıöçĞÜŞİÖÇ'
allowed_chars = set(turkish_chars)

def is_allowed_unicode(char):
    # ASCII, Türkçe karakter veya boşluk/newline ise izin ver
    if ord(char) < 128:  # ASCII
        return True
    if char in allowed_chars:  # Türkçe
        return True
    return False

# Kalan emoji'leri temizle
cleaned_content = ''.join(char if is_allowed_unicode(char) else ' ' for char in modified_content)

# Dosyaya yaz
with open(r'api\views.py', 'w', encoding='utf-8') as f:
    f.write(cleaned_content)

print("Emoji'ler temizlendi!")
print(f"Orijinal boyut: {len(content)} karakter")
print(f"Yeni boyut: {len(cleaned_content)} karakter")
