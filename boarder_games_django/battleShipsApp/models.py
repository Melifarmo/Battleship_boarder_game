from django.db import models
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView, View, RedirectView

# Create your models here.
User = get_user_model()


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    message = models.CharField(max_length=255)
    
# class BattleShipGame(models.Model):
#     first_player_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_player')
#     second_player_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_player')
#     datetime_of_start = models.DateTimeField(auto_now_add=True)
