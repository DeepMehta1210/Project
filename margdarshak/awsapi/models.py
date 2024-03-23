from django.db import models

class Zone(models.Model):
    zone_id = models.CharField(max_length=100, primary_key=True)
    zone_name = models.CharField(max_length=255)
    l1n1 = models.TextField()
    l2n2 = models.TextField()
    city_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class Area(models.Model):
    area_id = models.CharField(max_length=100, primary_key=True)
    area_name = models.CharField(max_length=255)
    l1n1 = models.TextField()
    l2n2 = models.TextField()
    zone_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class Cluster(models.Model):
    cluster_id = models.CharField(max_length=100, primary_key=True)
    cluster_name = models.CharField(max_length=255)
    l1n1 = models.TextField()
    l2n2 = models.TextField()
    area_id = models.CharField(max_length=100)
    zone_id = models.CharField(max_length=100)
    city_id = models.CharField(max_length=100)
    cedetive_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class WLSU(models.Model):
    wlsu_id = models.CharField(max_length=100, primary_key=True)
    wlsu_name = models.CharField(max_length=255)
    l1n1 = models.TextField()
    cedetive_id = models.CharField(max_length=100)
    wll = models.IntegerField()
    sqi = models.IntegerField()
    aqi = models.IntegerField()
    vl = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class Cedative(models.Model):
    cedative_id = models.CharField(max_length=100, primary_key=True)
    bl1n1 = models.TextField()
    bcedativeid = models.CharField(max_length=100)
    wlsu_id = models.CharField(max_length=100)
    cluster_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
