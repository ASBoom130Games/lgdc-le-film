from django.db import models
from django.utils import timezone
from precise_bbcode.fields import BBCodeTextField
from django.utils.safestring import mark_safe

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
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
	
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    icon = models.CharField(max_length=30, help_text=mark_safe('Consultez la liste des logo possible <a href="https://fontawesome.com/icons?d=gallery">ici</a>'))
    def __str__(self):
         return self.nom

class Descriptions(models.Model):
     title = models.CharField(max_length=200, verbose_name="titre")
     corp = BBCodeTextField(verbose_name="texte")
     
     def __str__(self):
          return self.title
		
class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = BBCodeTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    article = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    livre = models.ForeignKey('Livres', on_delete=models.CASCADE, null=True)
    admin = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Livres(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    couverture = models.CharField(max_length=400, default = 'http://lgdclefilm.pythonanywhere.com/static/image/default_blanket.jpg')
    quatrieme_de_couverture = models.TextField()
    description = BBCodeTextField()
    auteur = models.CharField(max_length=100)
    date_en = models.CharField(max_length=200, verbose_name="date de parution anglaise")
    date_fr = models.CharField(max_length=200, verbose_name="date de parution française")
    cycle = models.ForeignKey('Cycle', on_delete=models.CASCADE)
    tome = models.CharField(max_length=2, help_text=mark_safe('chiffre entre 1 et 9, pour les HS mettre le numero de parution'))
    commentaires = models.BooleanField(default=False)
	
    def __str__(self):
        return self.titre

class Cycle(models.Model):
    titre = models.CharField(max_length=200)
    image = models.CharField(max_length=400, default = 'http://lgdclefilm.pythonanywhere.com/static/image/defaut_background.jpg')
    slogan = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.titre