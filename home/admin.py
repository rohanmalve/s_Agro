from django.contrib import admin
from home.models import Contact,Category,Post


class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','date')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('imagetag','title','description','url','add_date')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('imagetag','title','url')
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=10

# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)