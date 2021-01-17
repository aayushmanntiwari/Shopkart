from django.contrib import admin
import admin_thumbnails
from .models import Product,Image,Size,Color,Varient

# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name','code','color_tag']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','code']

class variantsAdmin(admin.ModelAdmin):
    list_display = ['title','product','color','size','price','quantity','image_tag']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','product','image']

class ProductVarientsInline(admin.TabularInline):
    model = Varient
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id',)
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','varient','seller','status']
    #readonly_fields = ('image_tag',)
    inlines = [ProductImageInline,ProductVarientsInline]  #this will basically show other model fields inside the current model
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Size,SizeAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Varient,variantsAdmin)