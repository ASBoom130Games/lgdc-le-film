from django import forms
from user.models import Profil
from .models import Post, Comment, Descriptions

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'resume', 'image_lien', 'Publique', 'text')

class ConnexionForm(forms.Form):
         username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Descriptions
        fields = ('corp',)
		
class InscriptionForm(forms.Form):
         username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         email = forms.CharField(label="Adresse email", max_length=60, widget=forms.TextInput(attrs={'type':"email", 'id':"defaultForm-email", 'class': 'form-control form-control-sm validate'}))
         password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
         password2 = forms.CharField(label="Répeter mot de passe", widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': "form-control pl-3 pt-3",  'placeholder': "Ecrivez quelque chose ici...", 'rows': 6,'id':"text",},)
        }
		
class ProfilForm(forms.ModelForm):

    class Meta:
        model = Profil
        fields = ('image_lien',)
        widgets = {
            'image_lien': forms.TextInput(attrs={'type':"text", 'id':"form29", 'class':"form-control form-control-sm validate ml-0",},)
        }