from django.contrib import admin
from .models import Post

admin.site.site_header = "GDSC BLOG Admin(Sena)"

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'author']
    raw_id_fields = ['author']
    ordering = ['status', 'publish']


