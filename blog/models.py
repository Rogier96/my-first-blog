from django.db import models
from django.utils import timezone

# Create your models here.
# copied from https://tutorial.djangogirls.org/en/django_models/
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    recipe = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()
    email = models.CharField(max_length=200)
    """image = models.ImageField(upload_to = 'static/pictures')"""
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
