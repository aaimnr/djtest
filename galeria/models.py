from django.db import models

class Dywan(models.Model):
    name = models.CharField(max_length=30)
    dlugosc = models.PositiveIntegerField()
    szeroskosc = models.PositiveIntegerField()
    #zdjecia = models.OneToManyField("Zdjecie")

    def __unicode__(self):
        return self.name
    
class Zdjecie(models.Model):
    dywan = models.ForeignKey(Dywan)
    zdjecie = models.ImageField(upload_to="media/")   
# Create your models here.
