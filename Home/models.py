from django.db import models
from django.utils.text import slugify

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

class Post(models.Model):
    version = models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title