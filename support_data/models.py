# tweet/models.py
from django.db import models
from user.models import User

# Create your models here.
class Support(models.Model):

    team_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "images/")
    people_num = models.CharField(max_length=128)