from django.db import models
from django.contrib.auth.models import User

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    class Meta:
        ordering = ["-created_at"]
        
    def __str__(self):
        return self.content
