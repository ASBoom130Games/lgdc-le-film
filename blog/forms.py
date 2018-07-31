from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'resume', 'image_lien', 'Publique', 'text')

class ConnexionForm(forms.Form):
         username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
		 
class ConnexionForm(forms.Form):
         username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
		 
class InscriptionForm(forms.Form):
         username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         email = forms.CharField(label="Adresse email", max_length=60, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
         password2 = forms.CharField(label="Répeter mot de passe", widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)