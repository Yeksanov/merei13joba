from django.db import models
from django.urls import reverse

class Form(models.Model):
    Aty = models.CharField(max_length = 50 )
    Tegi = models.CharField(max_length = 50)
    Jasy = models.CharField(max_length = 50)
    TýǵanQalasy = models.CharField(max_length = 50)
    Uıalytelefon = models.CharField(max_length = 50)
    Sýreti= models.ImageField()
    Elektrondypochta = models.EmailField(blank = True)
    Ózitýralyanyqtama = models.TextField(default = 'Anyqtama')
    def __str__(self):
        return self.Aty

class Person(models.Model):
    title = models.CharField('Name', max_length=50)
    person = models.TextField('Description')

    def str(self):
        return self.person


class Person1(models.Model):
    title = models.CharField('Name', max_length=50)
    person = models.TextField('Description')


    def str(self):
        return self.person



class Person2(models.Model):
    title = models.CharField('Name', max_length=50)
    person = models.TextField('Description')

    def str(self):
        return self.person

class Person3(models.Model):
    title = models.CharField('Name', max_length=50)
    person = models.TextField('Description')

    def str(self):
        return self.person

class city(models.Model):
    title = models.CharField('Name', max_length=50)
    person = models.TextField('Description')

    def str(self)\
            :
        return self.person

