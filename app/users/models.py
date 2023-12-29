from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 25)
    password = models.CharField(max_length = 24)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']