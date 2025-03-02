from django.db import models
from apps.camp.models import Camp, Area
from apps.housing.models import HousingArea

class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE, related_name="programs")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def update_dates(self) -> None:
        """Automatically set start_date and end_date based on sessions"""
        sessions = self.sessions.all().order_by("start_time")
        if sessions.exists():
            self.start_date = sessions.first().start_time.date()
            self.end_date = sessions.last().end_time.date()
            self.save()

    def __str__(self) -> str:
        return f"{self.name} ({self.camp.name})"
    
class Session(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="sessions")
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # TODO --> merit_badges = models.ManyToManyField(MeritBadge, blank=True, related_name="sessions")
    housing_areas = models.ManyToManyField(HousingArea, blank=True, related_name="sessions")

    def save(self, *args, **kwargs) -> None:
        """Ensure Program dates are updated whenever a session is created or modified"""
        super().save(*args, **kwargs)
        self.program.update_dates()

    def __str__(self) -> str:
        return f"{self.name} ({self.program.name})"

