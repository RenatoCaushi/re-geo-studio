from django.contrib import admin
from .models import Sherbimi

@admin.register(Sherbimi)
class SherbimiAdmin(admin.ModelAdmin):
    list_display = ('titulli', 'renditja', 'ikona_bootstrap')
    prepopulated_fields = {'slug': ('titulli',)}
    list_editable = ('renditja',)
