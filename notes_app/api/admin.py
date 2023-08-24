from django.contrib import admin
from .models import Notes
# Register your models here.

admin.site.register(Notes)

class NotesModelAdmin(admin.ModelAdmin):
    list_display=('title','text')



