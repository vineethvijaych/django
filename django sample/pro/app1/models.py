from django.db import models

# Create your models here.

class student(models.Model):
    student_id =models.IntegerField()
    student_name =models.CharField(max_length=20)
    course_name =models.CharField(max_length=20)
    lname = models.CharField(max_length=20,null=True)
    
    
    

class pictures(models.Model):
    img=models.ImageField(upload_to="mypics/")





