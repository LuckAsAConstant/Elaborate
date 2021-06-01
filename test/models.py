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

class Accumulations(models.Model):
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
    idAccumulations = models.ForeignKey(Accumulations, on_delete=models.CASCADE)


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
    idAccumulation = models.ForeignKey(Accumulations, on_delete=models.CASCADE)
    status = models.BooleanField()

    
class Trellis(models.Model):
    Status = models.BooleanField()
    name = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    idLine = models.ForeignKey(Line, on_delete=models.CASCADE)

# class Users(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     Admin = models.BooleanField()
#     name = models.CharField(max_length=30)
#     surname = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
    # def __str__(self):
    #     return '%s %s %f %f' % (self.active, self.name, self.longitude, self.latitude)    


            
