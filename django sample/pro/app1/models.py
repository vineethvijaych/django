from django.db import models

# Create your models here.

class student(models.Model):
    student_id =models.IntegerField()
    student_name =models.CharField(max_length=20)
    course_name =models.CharField(max_length=20)
    
    def __str__(self):
        return self.student_name