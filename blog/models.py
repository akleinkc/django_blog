#this is a comment
from django.db import models
from django.utils import timezone

#Post is the name of our model.  Means Post is a django model 
#and django knows it needs to save it to a database.  Defining the things stored
#field type options https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#the def is defining a method which is publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title