from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    rating = models.IntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    def __str__(self):
     return f"{self.first_name}, {self.last_name}({self.age})"