from django.db import models
from django.utils import timezone
from precise_bbcode.fields import BBCodeTextField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    #image = models.ImageField(upload_to = 'image/', default = 'image/affiche-warriors-movie.jpeg' )
    image_lien = models.CharField(max_length=400, default = 'https://pmcvariety.files.wordpress.com/2016/11/warriors-20161120_092416-med-ret.jpg?w=1000&h=563&crop=1')
    resume = models.CharField(max_length=100)
    text = BBCodeTextField()
    Publique = models.BooleanField(default=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
