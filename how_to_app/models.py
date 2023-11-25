from django.db import models
from django.urls import reverse

# Create your models here.

class HowToUserVehicle(models.Model):

    YEAR = (
            ('2015', '2015'),
            ('2016', '2016'),
            ('2017', '2017'),
            ('2018', '2018'),
            ('2019', '2019'),
            ('2020', '2020'),
            ('2021', '2021'),
            ('2022', '2022'),
            )

    MAKE = (
            ('Ford', 'Ford'),
            ('Chevy', 'Chevy'),
            ('Dodge', 'Dodge'),
            )

    year = models.CharField(max_length=200, choices=YEAR)
    make = models.CharField(max_length=200, choices=MAKE)
    model = models.CharField(max_length=200)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse("vehicle-detail", args=[str(self.id)])
    
class HowToUser(models.Model):

    first_name = models.CharField("First Name", max_length=200)
    last_name = models.CharField("Last Name", max_length=200)
    email = models.CharField("Email", max_length=200)
    vehicle = models.OneToOneField(HowToUserVehicle, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse("HowToUser-detail", args=[str(self.id)])
    
