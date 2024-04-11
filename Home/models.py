from django.db import models

# Create your models here.
class Introduction(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
class Description(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    about1 = models.CharField(max_length=500)
    about2 = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    sno = models.AutoField(primary_key=True)
    skill1 = models.CharField(max_length=250)
    skill2 = models.CharField(max_length=250)
    skill3 = models.CharField(max_length=250)
    skill4 = models.CharField(max_length=250)
    skill5 = models.CharField(max_length=250)
    skill6 = models.CharField(max_length=250)
    skill7 = models.CharField(max_length=250)
    skill8 = models.CharField(max_length=250)
    skill9 = models.CharField(max_length=250)
    skill10 = models.CharField(max_length=250)

    def __str__(self):
        return self.skill1

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Project1(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Project2(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Project3(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title