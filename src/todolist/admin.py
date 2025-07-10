from django.contrib import admin
from .models import NoteModel
# Register your models here.

@admin.register(NoteModel)
class NoteMadmin(admin.ModelAdmin):
    pass