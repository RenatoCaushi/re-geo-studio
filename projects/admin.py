from django.contrib import admin
from .models import Projekti

@admin.register(Projekti)
class ProjektiAdmin(admin.ModelAdmin):
    list_display = ('titulli', 'vendi', 'klienti', 'data_perfundimit')
    prepopulated_fields = {'slug': ('titulli',)}
    list_filter = ('vendi', 'data_perfundimit')
    search_fields = ('titulli', 'vendi', 'klienti')
