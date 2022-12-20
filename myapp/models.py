from django.db import models
from django.contrib.auth.models import AbstractUser

class ulimiter(models.Model):
    #creating database table (makemigrations means create changes and store in a file)
    #________________________(migrate means apply the pending changes created by makemigrations)
    uid=models.TextField() 
    ulimit=models.IntegerField(default=0)
    
    def __str__(self):
        return self.uid



# Create your models here.
class Contect(models.Model):
    #creating database table (makemigrations means create changes and store in a file)
    #________________________(migrate means apply the pending changes created by makemigrations)
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField() 
    date=models.DateField()

    #to change the view of representation of tables in admin page
    def __str__(self):
        return self.name
class Poll(models.Model):
    loguser =models.CharField(max_length=30, default="admin")
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    def __str__(self):
        return self.question
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count


#class marked(models.Model):
#    has_answered = models.ManyToManyField(User)
#    question_text = models.CharField(max_length=80)