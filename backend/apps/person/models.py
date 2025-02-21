from datetime import date
from django.db import models

# Create your models here.
class Person(models.Model):

    # Define choices for fields below
    GENDER_CHOICES: tuple = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    YPT_CLASS_CHOICES: tuple = (
        ('Y', 'Under 18'),
        ('YA', '18-21'),
        ('A', '21+'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    email = models.EmailField()
    date_of_birth = models.DateField(default=date.today)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    # Calculated based on date of birth
    ypt_class = models.CharField(max_length=2, choices=YPT_CLASS_CHOICES, editable=False, default='Y')


    def save(self, *args, **kwargs):
        # Calculate the person's age based on the date_of_birth.
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
            # Set ypt_class based on the calculated age.
            if age < 18:
                self.ypt_class = 'Y'
            elif age < 21:
                self.ypt_class = 'YA'
            else:
                self.ypt_class = 'A'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"