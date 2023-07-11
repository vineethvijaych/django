from django.db import models

# Create your models here.


class student(models.Model): 
    id_no = models.IntegerField()
    sname = models.CharField(max_length=20) 
   
    cname = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.sname

class department(models.Model):
    dname = models.CharField(max_length=20)

    def __str__(self):
        return self.dname 


