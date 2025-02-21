from django.db import models

class HousingArea(models.Model):
    """
    Represents a housing area.
    """
    name = models.CharField(max_length=100)
    num_bathrooms = models.PositiveIntegerField()
    num_showers = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cabin(models.Model):
    """
    A cabin within a housing area.
    """
    housing_area = models.ForeignKey(
        HousingArea, 
        on_delete=models.CASCADE, 
        related_name='cabins'
    )
    name = models.CharField(max_length=100)
    has_heating = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.housing_area.name})"


class Room(models.Model):
    """
    A room in a cabin.
    """
    cabin = models.ForeignKey(
        Cabin, 
        on_delete=models.CASCADE, 
        related_name='rooms'
    )
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} in {self.cabin.name}"