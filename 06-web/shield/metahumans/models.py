from django.db import models
  
# Create your models here.

class Team(models.Model):

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    name = models.CharField(max_length=220)
    description = models.TextField(max_length=4000)
    headquarter =  models.CharField(max_length=100)

    def __str__(self):
        return self.name


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

class Team(models.Model):

    class Meta: # Metainformación del model, información importante pero que no forma parte del modelo
        verbose_name = "Equipo" # cuando hablamos de esta entidad, los humanos hablamos de equipo
        verbose_name_plural = "Equipos" # cuando hablamos de esta entidad, los humanos hablamos de equipos

    name = models.CharField(max_length=220)
    description = models.TextField(max_length=4000)
    headquarter =  models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MetaHuman(models.Model):
    name = models.CharField(max_length=42)
    country = models.CharField(max_length=22, choices=COUNTRIES)
    level = models.IntegerField(default=10)
    active = models.BooleanField(default=True)
    powers = models.ManyToManyField(Power)
<<<<<<< HEAD
    ally = models.BooleanField(max_length=22, default=True)
    last_update = models.DateTimeField(auto_now=True)
    team = models.ForeignKey( # Many to One
            Team, # modelo de referencia
            on_delete=models.PROTECT, 
            blank=True, # me permite que un superhéoe pueda estar o no asociado a un equipo
            null=True, # para estos casos donde no hay equipo, ponme un null
            default=None, # y por defecto, cuando cree un superhéroe no va a estar asociado a ningun grupo
        )
=======
    last_update = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        default=None,
    )
>>>>>>> 962ff782e31f1673615e4e69fa766cd5febe78db

    def __str__(self):
        return self.name

