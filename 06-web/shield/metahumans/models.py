from django.db import models
<<<<<<< HEAD
  
=======

>>>>>>> 6948fa3ec2bf31c512f81f78cab02690591b5d62
# Create your models here.

class Power(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    level = models.IntegerField(default=50)

    def __str__(self):
        return f'{self.name}: {self.description}'

<<<<<<< HEAD
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
=======

COUNTRIES = [
    ('US', 'United states'),
    ('ES', 'Spain'),
    ('UK', 'United Kingdom'),
    ('OT', "Others"),
    ]

class MetaHuman(models.Model):
    name = models.CharField(max_length=42)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    level = models.IntegerField(default=10)
    active = models.BooleanField(default=True)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name
>>>>>>> 6948fa3ec2bf31c512f81f78cab02690591b5d62
