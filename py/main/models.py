from django.db import models

# Create your models here.


class User(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25,blank=True,null=True)
    age=models.PositiveIntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.first_name
    


