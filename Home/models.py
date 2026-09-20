from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveBigIntegerField()
    description = models.TextField()
    skills = models.CharField(max_length=100)
    website_link = models.URLField(max_length=2000)
    pdf = models.FileField(upload_to='projects/pdfs/',blank=True, null=True)

    def __str__(self):
        return self.title