from django.db import models
from django.utils import timezone
# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(default=timezone.now)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name