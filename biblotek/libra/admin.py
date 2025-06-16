from django.contrib import admin
from .models import Libri

@admin.register(Libri)
class LibriAdmin(admin.ModelAdmin):
    list_display = ('titulli', 'autori', 'viti_publikimit')
    search_fields = ('titulli', 'autori')
