from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the car make
    description = models.TextField()  # Description of the car make
    # Add any other fields you would like to include in a car make

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship with CarMake
    dealer_id = models.IntegerField()  # Refers to a dealer created in the Cloudant database
    name = models.CharField(max_length=100)  # Name of the car model

    # Choices for the car type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Type of the car model

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )  # Year of the car model

    # Add any other fields you would like to include in a car model

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"  # Return the car make and car model as the string representation
