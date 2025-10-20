from django.db import models
from course.models import Course

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    date_of_birth = models.DateField()

    courses = models.ManyToManyField(Course, through='StudentCourse', related_name='students')

    def __str__(self):
        return self.name

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course  = models.ForeignKey(Course,  on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')  
