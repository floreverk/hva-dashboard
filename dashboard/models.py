from django.db import models
from django_countries.fields import CountryField

# Create your models here. - check models documentation for datatypes
SECTOR_CHOICES = (
    ('media','Media'),
    ('cultuur', 'Cultuur'),
    ('particulier','Particulier'),
    ('onderwijs','Onderwijs'),
    ('welzijn','Welzijn'),
)

class imagerequest(models.Model):
    idnumber = models.CharField(max_length=10, default='BA2022-###', unique=True)
    year = models.DateField(default='YYYY-MM-DD')
    origin_country = CountryField(blank_label='(select country)')
    origin_province = models.CharField(max_length=50, blank=True, null=True)
    origin_city = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField()
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES, default='media')
    medium_foto = models.IntegerField(blank=True, null=True)
    medium_digitalfoto = models.IntegerField(blank=True, null=True)
    medium_document = models.IntegerField(blank=True, null=True)
    medium_reclame = models.IntegerField(blank=True, null=True)
    medium_film = models.IntegerField(blank=True, null=True)
    medium_audio = models.IntegerField(blank=True, null=True)
    medium_digitalarchive = models.IntegerField(blank=True, null=True)
    medium_objectfoto = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.idnumber

BUGS_CHOICES = (
    ('spin', 'Spin'),
    ('mot', 'Mot'),
    ('kleermot', 'Kleermot'),
    ('vlieg', 'Vlieg'),
    ('pissebed', 'Pissebed'),
    ('fruitvlieg', 'Fruitvlieg'),
    ('mug', 'Mug'),
    ('vliegendemier', 'Vliegende mier'),
)

ROOM_CHOICES = (
    ('opstaan', 'Opstaan'),
    ('geboorte', 'Geboorte'),
    ('verhuizen', 'Verhuizen'),
    ('rustdag', 'Rustdag'),
    ('ongeluk', '(on)geluk'),
    ('rouwen', 'Rouwen'),
    ('ouder', 'Ouder'),
    ('trappenhal', 'Trappenhal'),
    ('jong', 'Jong'),
    ('vakantie', 'Vakantie'),
    ('school', 'School'),
    ('trouw', 'Trouw'),
    ('avond', 'Avond'),
    ('huishouden', 'Huishouden'),
    ('spelen', 'Spelen'),
)

class bugs(models.Model):
    idnumber = models.CharField(max_length=10, default='BU2022-###', unique=True)
    year = models.DateField(default='YYYY-MM-DD')
    bug = models.CharField(max_length=50, choices=BUGS_CHOICES, default='spin')
    room = models.CharField(max_length=50, choices=ROOM_CHOICES, default='spin')
    quantity = models.IntegerField()

    def __str__(self):
        return self.idnumber