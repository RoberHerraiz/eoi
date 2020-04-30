from django.db import models
  
# Create your models here.

class Power(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    level = models.IntegerField(default=50)

    def __str__(self):
        return f'{self.name}: {self.description}'

COUNTRIES = [
    ('US', 'United States'),
    ('ES', 'Spain'),
    ('UK', 'United Kingdom'),
    ('OT', 'Others'),
    ]


class MetaHuman(models.Model):
    name = models.CharField(max_length=42)
    country = models.CharField(max_length=22, choices=COUNTRIES)
    level = models.IntegerField(default=10)
    active = models.BooleanField(default=True)
    powers = models.ManyToManyField(Power)
    ally = models.BooleanField(max_length=22, default=True)

    def __str__(self):
        return self.name