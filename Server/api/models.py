from django.db import models

class Message(models.Model):
    """Basit bir mesaj modeli - Flutter uygulamasıyla test için"""
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"
    
    def __str__(self):
        return self.title
