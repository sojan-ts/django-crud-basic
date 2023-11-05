from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        app_label = 'mycrudapp'  # Add this line to specify the app_label
