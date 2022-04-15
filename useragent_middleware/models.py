from django.db import models


class devices(models.Model):
    windows = models.IntegerField()
    iphone = models.IntegerField()
    mac = models.IntegerField()
    android = models.IntegerField()
    other = models.IntegerField()
