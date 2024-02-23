from django.contrib.auth.models import User
from django.db import models

class History(models.Model):
    english = models.TextField()
    hindi = models.TextField()

class LTSAPIToken(models.Model):
    user = models.OneToOneField(
        User,
        related_name="ltsapitoken",
        on_delete=models.CASCADE
    )
    
    # create uuid4 string
    # and assign it to token
    token = models.CharField(max_length=36)

    def __str__(self) -> str:
        return self.user.username