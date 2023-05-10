from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Malumot(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    audio = models.CharField(max_length=500)
    text = models.TextField()
    img = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('details',args=[str(self.pk)])
