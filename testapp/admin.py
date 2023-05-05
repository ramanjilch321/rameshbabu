from django.contrib import admin
from .models import Logo_Image,Contact_Info,Students_new
# Register your models here.
class SAdmin(admin.ModelAdmin):
    list_display = ['img','n1','n2','n3','n4']
admin.site.register(Logo_Image,SAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['mobile_number','email','address']
admin.site.register(Contact_Info,ContactAdmin)

admin.site.register(Students_new)