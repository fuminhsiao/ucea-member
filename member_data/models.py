from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    university_id = models.CharField(max_length=100)
    cx = models.FloatField()
    cy = models.FloatField()
    facebook_id = models.CharField(max_length=100, blank=True, null=True)
    twitter_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    official_website = models.URLField(blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name