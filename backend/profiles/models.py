from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# A model for the users profile

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Parent', 'Parent'),
        ('Child', 'Child'),
    ]
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    household = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.member} is a {self.parent} in the {self.household} household"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(member=instance)

post_save.connect(create_profile, sender=User)