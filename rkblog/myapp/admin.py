from django.contrib import admin
from .models import Post,comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

class commentAdmin(admin.ModelAdmin):
    list_display=['name','email','created','updated','active']
    list_filter=('name','created','active')


admin.site.register(comment,commentAdmin)