from django.contrib import admin

# Register your models here.
from apps.turno.models import Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ("cliente","barberia",)
    search_fields = ('cliente',)
    list_filter = ('cliente',)