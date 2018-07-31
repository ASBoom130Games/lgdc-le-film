from django.contrib import admin
from .models import Post, Comment
from django.utils.text import Truncator

class CommentAdmin(admin.ModelAdmin):
    list_display   = ('title', 'apercu_contenu', 'published_date')
    def apercu_contenu(self, text):
        return Truncator(text.text).chars(20, truncate='...')
		
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)