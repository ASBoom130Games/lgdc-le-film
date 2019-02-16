from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment, Descriptions, Livres, Cycle
from user.models import Profil
from .forms import PostForm, ConnexionForm, InscriptionForm, CommentForm, DescriptionForm, ProfilForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage
from django.utils.text import Truncator
import datetime
import logging

logger = logging.getLogger(__name__)

def post_list(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    error = False
    errormdp = False
    home = True
    drafts = posts.filter(Publique=False)
    if request.method == "POST":
         form = ConnexionForm(request.POST)
         new = InscriptionForm(request.POST)
         if form.is_valid():
              name = request.POST.get('username')
              password = request.POST.get('password')
              user = authenticate(username=name, password=password)  # Nous vérifions si les données sont correctes
              
              if user:  # Si l'objet renvoyé n'est pas None
                   login(request, user)  # nous connectons l'utilisateur
              else: # sinon une erreur sera affichée
                   error = True
         if new.is_valid():
              nom = request.POST.get('username')
              email = request.POST.get('email')
              mdp = request.POST.get('password')
              mdp2 = request.POST.get('password2')
              
              if mdp == mdp2:  # Si les mots de passes sont correctes
                   nouveau = User.objects.create_user(nom, email, mdp)
                   nouveau.is_staff = False
                   nouveau.is_superuser = False
                   nouveau.save()
                   login(request, nouveau) 
              else:
                   errormdp = True
                   error = False
    else:
         form = ConnexionForm(request.POST)
         new = InscriptionForm(request.POST)
    return render(request, 'blog/post_list.html', {'posts': posts, 'form' : form, 'error':error, 'new' : new, 'errormdp' : errormdp, 'home':home, 'drafts':drafts, 'profil':profil})
	
def google(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

def post_detail(request, pk):
    home = False
    com_profil = Profil.objects.all
    post = get_object_or_404(Post, pk=pk)
    if post.Publique :   
        for perso in User.objects.filter(username='Anonyme'):
	        lol = perso
        if request.user.is_authenticated:
            profil = get_object_or_404(Profil, author=request.user)
        else:
            profil = get_object_or_404(Profil, author=lol)
        commentaires = Comment.objects.filter(article__title=post.title)
        len = commentaires.count ()
        resume = Truncator(post.text).chars(40, truncate='...')
        if request.method == "POST":
        	form = CommentForm(request.POST)
        	if form.is_valid():
        	    article = post.title
        	    comment = form.save(commit=False)
        	    if request.user.is_authenticated:
        	        comment.author = request.user
        	    else:
        	        comment.author=lol
        	    comment.title = request.user
        	    comment.created_date=timezone.now()
        	    comment.published_date=timezone.now()
        	    comment.article=post
            #if request.user.is_staff():
            #    comment.admin = True
            #else:
            #    comment.admin = False
        	    comment.save()
        else:
            form = CommentForm() 
        return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'commentaires':commentaires, 'len':len, 'resume':resume, 'profil':profil, 'com_profil':com_profil})
    else :
        return render(request, 'default/error_permission.html', {'post': post})

def post_new(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    height = 460
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'height':height, 'profil':profil})
	
def post_edit(request, pk):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    post = get_object_or_404(Post, pk=pk)
    height = 460
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'height':height, 'profil':profil})

def description_edit(request, pk):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    post = get_object_or_404(Descriptions, pk=pk)
    if request.method == "POST":
        form = DescriptionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/'+post.title)
    else:
        form = DescriptionForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'profil':profil})
			
def deconnexion(request):
    logout(request)
    return redirect(reverse(post_list))
	
def film(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    film = True
    resume = "decouvrez toute l'info du film de la Guerre des Clans !"
    description = get_object_or_404(Descriptions, title="Film")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/film.html', {'posts': posts, 'description':description, 'film':film, 'resume':resume, 'profil':profil})
	
def info(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    description = get_object_or_404(Descriptions, title="Information")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/film.html', {'posts': posts, 'description':description, 'profil':profil})
	
def serie(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    serie = True
    cycle = Cycle.objects.all
    livres = Livres.objects.all
    resume = "decouvrez toute l'info sur les livres de la Guerre des Clans !"
    description = get_object_or_404(Descriptions, title="Serie")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = posts.filter(published_date__gte=datetime.datetime(2018, 3, 18))
    return render(request, 'blog/serie.html', {'posts': posts, 'description':description, 'serie':serie, 'cycle':cycle, 'livres':livres, 'resume':resume, 'profil':profil})

def livre_details(request, pk, slug):
	com_profil = Profil.objects.all
	livre = get_object_or_404(Livres, pk=pk)
	for perso in User.objects.filter(username='Anonyme'):
		lol = perso
	if request.user.is_authenticated:
		profil = get_object_or_404(Profil, author=request.user)
	else:
		profil = lol
	commentaires = Comment.objects.filter(livre__titre=livre.titre)
	len = commentaires.count ()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			book = livre
			comment = form.save(commit=False)
			if request.user.is_authenticated:
				comment.author = request.user
			else:
				comment.author=lol
			comment.title = request.user
			comment.created_date=timezone.now()
			comment.published_date=timezone.now()
			comment.livre=book
			comment.save()
	else:
		form = CommentForm() 
			
	return render(request, 'blog/livre.html', {'livre': livre , 'commentaires':commentaires, 'len':len, 'form': form, 'profil':profil, 'com_profil':com_profil})	

def brouillons(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    if request.user.is_staff :
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        posts = posts.filter(Publique=False)
        return render(request, 'blog/broullion.html', {'posts': posts})	
    else :
        return render(request, 'default/error_permission.html')	

def connexion(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
    else:
        profil = 0
    nobr = True
    error = False
    if request.method == "POST":
          form = ConnexionForm(request.POST)
          if form.is_valid():
               name = request.POST.get('username')
               password = request.POST.get('password')
               user = authenticate(username=name, password=password)  # Nous vérifions si les données sont correctes
               if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # nous connectons l'utilisateur
                    return redirect('post_list')
               else: # sinon une erreur sera affichée
                   error = True
    else:
         form = ConnexionForm()
    return render(request, 'default/authentification.html', {'form': form, 'nobr':nobr, 'error':error})	

def inscription(request):
    nobr = True
    errormdp = False
    errorname = False
    if request.method == "POST":
        new = InscriptionForm(request.POST)
        if new.is_valid():
            nom = request.POST.get('username')
            email = request.POST.get('email')
            mdp = request.POST.get('password')
            mdp2 = request.POST.get('password2')
            if mdp == mdp2:  # Si les mots de passes sont correctes
                try:
                    obj = User.objects.get(username=nom)
                    errorname = True
                except User.DoesNotExist:
                    nouveau = User.objects.create_user(nom, email, mdp)
                    nouveau.is_staff = False
                    nouveau.is_superuser = False
                    nouveau.save()
                    login(request, nouveau) 
                    profil = Profil.objects.create(author=request.user)
                    profil.save()
            else:
                errorname = False
                errormdp = True
    else:
        new = InscriptionForm()
    return render(request, 'default/inscription.html', {'new': new, 'nobr':nobr, 'errormdp':errormdp, 'errorname':errorname})
	
def profil(request):
    if request.user.is_authenticated:
        profil = get_object_or_404(Profil, author=request.user)
        if request.method == "POST":
            form = ProfilForm(request.POST, instance=profil)
            if form.is_valid():
                profil = form.save()
        else:
            if profil.image_lien == "https://bit.ly/2X8ehxe":
                form = ProfilForm()
                logger.error('{{Information Utilisater}} Un utilisateur sans image de profil vient de consulter son profil')
            else:
                form = ProfilForm(instance=profil)
        return render(request, 'blog/user_settings.html', {'profil':profil, 'form':form})
    else:
        return render(request, 'default/error_permission.html')