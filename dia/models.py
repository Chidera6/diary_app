from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category

class Contents(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    categories = models.ForeignKey('Category',on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title



    