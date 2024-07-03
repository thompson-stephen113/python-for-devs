from django.db import models

# Create your models here.
class Customer(models.Model):
    # Class attributes
    name = models.CharField(max_length=120)
    notes = models.TextField(default="no notes...")
    pic = models.ImageField(upload_to="customers", default="no_picture.jpg")

    # String representation
    def __str__(self):
        return str(self.name)
