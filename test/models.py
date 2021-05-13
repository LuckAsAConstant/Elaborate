from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Region(models.Model):
    name = models.CharField(max_length=30)
    # def __str__(self):
    #     return '%s' % (self.name)

class City(models.Model):
    name = models.CharField(max_length=30) 
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)

    # def __str__(self):
    #     return '%s' % (self.name) 

class Central(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    idCity = models.ForeignKey(City, on_delete=models.CASCADE)

    # def __str__(self):
    #     return '%s %s' % (self.name, self.location)

class Line(models.Model):
    name = models.CharField(max_length=30)
    beginLongitude = models.FloatField()
    beginLatitude = models.FloatField()
    endLongitude = models.FloatField()
    endLatitude = models.FloatField()
    nameCabinet = models.CharField(max_length=30)
    placeCabinet = models.CharField(max_length=30)
    idCentral = models.ForeignKey(Central, on_delete=models.CASCADE)
    active = models.BooleanField()

    # def __str__(self):
    #     return '%s %f %f %s %s' % (self.name, self.begin, self.end, self.nameCabinet, self.placeCabinet)
    
    
class trellis(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    idLine = models.ForeignKey(Line, on_delete=models.CASCADE)

    # def __str__(self):
    #     return '%s %s %f %f' % (self.active, self.name, self.longitude, self.latitude)    


            
