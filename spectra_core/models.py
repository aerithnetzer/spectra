from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)
    # Institutional affiliation
    affiliation = models.CharField(max_length=200)
    # Email address
    email = models.EmailField()
    

class Author_Links(models.Model):
    # Links to author profiles
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    link = models.URLField()

class Keyword(models.Model):
    # Keyword(s) associated with a work to facilitate search
    keyword = models.CharField(max_length=200)

# Defines the work - the main model of the application
class Work(models.Model):
    # Define the fields of the work model
    # Title of work
    title = models.CharField(max_length=500)
    # Authors of work
    authors = models.ManyToManyField(Author)
    # Abstract of work
    abstract = models.TextField()
    # Date of publication
    publication_date = models.DateField()
    # Data management plan
    dmp = models.TextField()
    # URL to article
    url = models.URLField()
    # URL to codebase
    code_url = models.URLField()
    # URL to dataset
    dataset_url = models.URLField()
    # Keywords associated with work
    keywords = models.ManyToManyField(Keyword)
    # User who created the work
    creator = models.ForeignKey(User, on_delete=models.CASCADE)