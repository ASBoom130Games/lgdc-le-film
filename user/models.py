from django.db import models

class Profil(models.Model):
    author = models.ForeignKey('auth.User')
    image_lien = models.CharField(max_length=400, default = 'https://bit.ly/2X8ehxe')

    def __str__(self):
        return self.author.username