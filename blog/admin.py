from django.contrib import admin
from .models import Post, Comment, Categorie, Descriptions

class CategorieAdmin(admin.ModelAdmin):
   list_display   = ('nom',)
   search_fields  = ('nom',)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Descriptions)