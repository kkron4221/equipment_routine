from django.db import models

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=200)
    equipment_amount = models.IntegerField(default=0)
