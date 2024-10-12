from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from households.models import Household

# A model for the users profile

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Parent', 'Parent'),
        ('Child', 'Child'),
    ]
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.member.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(member=instance)

post_save.connect(create_profile, sender=User)