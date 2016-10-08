from django.db import models

# Create your models here.
class Pokemon(models.Model):
    no =      models.IntegerField()
    name =    models.CharField(max_length=200)
    type1 =   models.CharField(max_length=200)
    type2 =   models.CharField(max_length=200)
    total =   models.IntegerField()
    hp =      models.IntegerField()
    attack =  models.IntegerField()
    defense = models.IntegerField()
    spatk =   models.IntegerField()
    spdef =   models.IntegerField()
    speed =   models.IntegerField()

    def __str__(self):
        return self.name
