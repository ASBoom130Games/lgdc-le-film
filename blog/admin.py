from django.contrib import admin
from .models import Post, Comment, Categorie, Descriptions, Livres, Cycle
from django.utils.text import Truncator

class CategorieAdmin(admin.ModelAdmin):
   list_display   = ('nom',)
   search_fields  = ('nom',)

class CommentAdmin(admin.ModelAdmin):
   list_display   = ('title', 'livre', 'article')
   search_fields  = ('title',)
   
   def apercu_contenu(self, Livres):
        return Truncator(Livres.quatrieme_de_couverture).chars(40, truncate='...')
   apercu_contenu.short_description = 'Aperçu du contenu'

class LivreAdmin(admin.ModelAdmin):
   list_display   = ('titre','cycle', 'apercu_contenu')
   search_fields  = ('titre',)
   list_filter    = ('cycle',)
   fieldsets = (
       ('Informations élémentaires',{
           'fields':('titre','cycle','tome', 'slug')
       }),
       ('Information générales',{
           'fields':('couverture','auteur', 'date_en', 'date_fr', 'quatrieme_de_couverture')
       }),
       ('Autres',{
           'fields':('commentaires','description',)
       })
   )
   
   def apercu_contenu(self, Livres):
        return Truncator(Livres.quatrieme_de_couverture).chars(40, truncate='...')
   apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Livres, LivreAdmin)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Descriptions)
admin.site.register(Cycle)