from django.db import models

class Shows(models.Model):
    show_title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    date = models.DateTimeField()
    description = models.TextField()