from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(
        max_length=40, 
        verbose_name="Kép címe"
    )
    
    image = models.ImageField(
        upload_to='photos/', 
        verbose_name="Fénykép"
    )
    
    uploaded_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Feltöltés ideje"
    )
    
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Tulajdonos"
    )

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

    class Meta:
        verbose_name = "Fénykép"
        verbose_name_plural = "Fényképek"
        ordering = ['-uploaded_at']