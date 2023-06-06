from django.db import models

# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 100)
    ranking = models.IntegerField()
    last_update = models.DateField(auto_now = True)
    def __str__(self):
        return self.name + ' ' + self.surname
    
    
class Games(models.Model):
    players = models.CharField(max_length = 200)
    result = models.CharField(max_length = 3)
    last_update = models.DateField(auto_now=True)
    def __str__(self):
        return self.players + ' | ' + self.result
    