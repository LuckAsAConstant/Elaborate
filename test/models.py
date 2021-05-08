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

class City(models.Model):
    name = models.CharField(max_length=30) 
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE) 

class Central(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    idCity = models.ForeignKey(Region, on_delete=models.CASCADE)

class Line(models.Model):
    name = models.CharField(max_length=30)
    begin = models.FloatField()
    end = models.FloatField()
    nameCabinet = models.CharField(max_length=30)
    placeCabinet = models.CharField(max_length=30)
    
    
class trellis(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    idLine = models.ForeignKey(Line, on_delete=models.CASCADE)
    