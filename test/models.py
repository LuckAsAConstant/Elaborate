from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=30)
    # def __str__(self):
    #     return '%s' % (self.name) 

class Central(models.Model):
    name = models.CharField(max_length=30)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    type = models.CharField(max_length=30)
    # def __str__(self):
    #     return '%s %s' % (self.name, self.location)

class Accumulation(models.Model):
    NameAccum = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    Status = models.BooleanField()
    NameTran = models.CharField(max_length=30)
    Tranlong = models.FloatField()
    Tranlat = models.FloatField()

class Cabinet(models.Model):
    type = models.CharField(max_length=30)
    Status = models.BooleanField()
    idAccumulations = models.ForeignKey(Accumulation, on_delete=models.CASCADE)


class Line(models.Model):
    nameLine = models.CharField(max_length=30)
    beginLongitude = models.FloatField()
    beginLatitude = models.FloatField()
    endLongitude = models.FloatField()
    endLatitude = models.FloatField()
    nameCabinet = models.CharField(max_length=30)
    placeCabinet = models.CharField(max_length=30)
    idCentral = models.ForeignKey(Central, on_delete=models.CASCADE)
    idCabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    idAccumulation = models.ForeignKey(Accumulation, on_delete=models.CASCADE)
    status = models.BooleanField()

    
class Pylon(models.Model):
    Status = models.BooleanField()
    name = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    idLine = models.ForeignKey(Line, on_delete=models.CASCADE)
            
