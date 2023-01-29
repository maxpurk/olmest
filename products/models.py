from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Product(models.Model): 
    name          = models.CharField(max_length=30)
    dateOfUpload  = models.DateField(blank=True, auto_now=True)
    price         = models.FloatField(blank = True)
    condition     = models.CharField(max_length = 30, blank = True)
    brand         = models.CharField(max_length = 30, blank=True)
    descriptionText = models.TextField(blank = True)
    available = models.BooleanField(blank=True)
    tags           = models.ManyToManyField(Tag, blank = True)

    def __str__(self):
        return f"Product with name: {self.name}"

    def get_tags(self):
        return self.tags.all()




