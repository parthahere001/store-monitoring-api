from django.db import models

class storeStatusModel (models.Model):
    store_id = models.BigIntegerField()
    status = models.CharField(max_length=50)
    timestamp_uct = models.DateTimeField(auto_now=False, auto_now_add=False)


class menuHoursModel(models.Model):
    store_id = models.BigIntegerField()
    start_time_local = models.TimeField(auto_now=False, auto_now_add=False)
    day_num = models.IntegerField()
    end_time_local = models.TimeField(auto_now=False, auto_now_add=False)

class timezoneModel(models.Model):
    store_id = models.BigIntegerField()
    timezone_str = models.CharField(max_length=100)

