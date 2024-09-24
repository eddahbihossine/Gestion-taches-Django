from django.contrib import admin

# Register your models here.
from .models import Tache
from django.utils import timezone
from django.utils.html import format_html , format_html_join
from django.utils.dateparse import parse_datetime
from datetime import timedelta , date


class TacheAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'finie', 'date_echeance', 'colored_date_echeance')
    readonly_fields = ('date_creation',)

   
    def __str__(self):
        return self.titre

admin.site.register(Tache , TacheAdmin)
    


