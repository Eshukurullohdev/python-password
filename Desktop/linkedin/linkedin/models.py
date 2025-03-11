from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class  Meta:
        ordering = ['-created_at']