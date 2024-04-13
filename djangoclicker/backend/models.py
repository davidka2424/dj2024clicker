from django.db import models
from django.contrib.auth.models import User

class Core(models.Model):
    user_data = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    # Другие поля вашей модели Core
