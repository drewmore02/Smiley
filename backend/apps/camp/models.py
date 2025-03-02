from django.db import models
from apps.person.models import Person

class Camp(models.Model):
    name = models.CharField(max_length=255)
    camp_director = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL, related_name="camps_directed"
    )

    def __str__(self) -> str:
        return self.name
    

class Area(models.Model):
    name = models.CharField(max_length=255)

    # TODO: use a library for geolocation data instead of JSONField
    geo_location = models.JSONField()  # Store latitude & longitude as a JSON fiel
    
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE, related_name="areas")
    director = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL, related_name="areas_directed"
    )
    assistant_director = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL, related_name="areas_assistant_directed"
    )
    staff = models.ManyToManyField(Person, blank=True, related_name="areas_staff")
    # TODO --> merit_badges = models.ManyToManyField("MeritBadge", blank=True, related_name="areas")

    def __str__(self) -> str:
        return f"{self.name} ({self.camp.name})"