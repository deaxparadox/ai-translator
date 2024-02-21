from django.db import models

class History(models.Model):
    english = models.TextField()
    hindi = models.TextField()