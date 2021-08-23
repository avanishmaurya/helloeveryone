from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
