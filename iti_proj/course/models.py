from django.db import models

class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.code} - {self.name}'
