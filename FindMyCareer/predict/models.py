from django.db import models

# Create your models here.

# First step to create a database to develope quation answer form. In which the fields required on the form will be stored in databae.

class GuessCareer(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.IntegerField()
    Option2 = models.IntegerField()
    Option3 = models.IntegerField()
    Option4 = models.IntegerField()
    Option5 = models.IntegerField()

