from django.contrib import admin
from .models import Article,Person

class AritcleAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','update_time')

admin.site.register(Article,AritcleAdmin)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_name',)

admin.site.register(Person,PersonAdmin)
