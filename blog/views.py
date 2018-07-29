from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ConnexionForm, InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    error = False
    errormdp = False
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
              else:
                   errormdp = True
                   error = False
    else:
         form = ConnexionForm(request.POST)
         new = InscriptionForm(request.POST)
    return render(request, 'blog/post_list.html', {'posts': posts, 'form' : form, 'error':error, 'new' : new, 'errormdp' : errormdp})
	
def google(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #imagestr = str(post.image)
    #image = imagestr.split('blog/static/')
    #post.image = (image[1])
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
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
    return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
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
    return render(request, 'blog/post_edit.html', {'form': form})
	
def deconnexion(request):
    logout(request)
    return redirect(reverse(post_list))