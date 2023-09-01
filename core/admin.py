from django.contrib import admin
from core.models import News,Setting,Category,Product

# Register your models here.

admin.site.register(Setting)
admin.site.register(Category)


@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'logo', 'price', 'category')
    



@admin.register(News)
class Newsadmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'update_at', 'like', 'dislike', 'views')
    search_fields = ('title', 'created_at') 
    list_filter = ('created_at', 'update_at')
    readonly_fields = ('like', 'dislike', 'views', 'created_at', 'update_at')


# Django appearance
admin.site.site_header = "My name is Intiqam"