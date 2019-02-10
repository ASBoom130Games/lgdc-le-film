from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment, Descriptions, Livres, Cycle
from .forms import PostForm, ConnexionForm, InscriptionForm, CommentForm, DescriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage
from django.utils.text import Truncator
import datetime

def post_list(request):
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
    return render(request, 'blog/post_list.html', {'posts': posts, 'form' : form, 'error':error, 'new' : new, 'errormdp' : errormdp, 'home':home, 'drafts':drafts})
	
def google(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

def post_detail(request, pk):
    home = False
    post = get_object_or_404(Post, pk=pk)
    if post.Publique :   
        for perso in User.objects.filter(username='Anonyme'):
	        lol = perso
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
        return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'commentaires':commentaires, 'len':len, 'resume':resume})
    else :
        return render(request, 'default/error_permission.html', {'post': post})

def post_new(request):
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
    return render(request, 'blog/post_edit.html', {'form': form, 'height':height})
	
def post_edit(request, pk):
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
    return render(request, 'blog/post_edit.html', {'form': form, 'height':height})

def description_edit(request, pk):
    post = get_object_or_404(Descriptions, pk=pk)
    if request.method == "POST":
        form = DescriptionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/'+post.title)
    else:
        form = DescriptionForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
			
def deconnexion(request):
    logout(request)
    return redirect(reverse(post_list))
	
def film(request):
    film = True
    resume = "decouvrez toute l'info du film de la Guerre des Clans !"
    description = get_object_or_404(Descriptions, title="Film")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/film.html', {'posts': posts, 'description':description, 'film':film, 'resume':resume})
	
def info(request):
    description = get_object_or_404(Descriptions, title="Information")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/film.html', {'posts': posts, 'description':description})
	
def serie(request):
    serie = True
    cycle = Cycle.objects.all
    livres = Livres.objects.all
    resume = "decouvrez toute l'info sur les livres de la Guerre des Clans !"
    description = get_object_or_404(Descriptions, title="Serie")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = posts.filter(published_date__gte=datetime.datetime(2018, 3, 18))
    return render(request, 'blog/serie.html', {'posts': posts, 'description':description, 'serie':serie, 'cycle':cycle, 'livres':livres, 'resume':resume})

def livre_details(request, pk, slug):
    livre = get_object_or_404(Livres, pk=pk)
    for perso in User.objects.filter(username='Anonyme'):
        lol = perso
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
			
    return render(request, 'blog/livre.html', {'livre': livre , 'commentaires':commentaires, 'len':len, 'form': form})	

def brouillons(request):
    if request.user.is_staff :
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        posts = posts.filter(Publique=False)
        return render(request, 'blog/broullion.html', {'posts': posts})	
    else :
        return render(request, 'default/error_permission.html')	

def connexion(request):
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
    if request.method == "POST":
        new = InscriptionForm(request.POST)
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
    else:
        new = InscriptionForm()
    return render(request, 'default/inscription.html', {'new': new, 'nobr':nobr, 'errormdp':errormdp})	