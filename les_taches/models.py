

from django.db import models
from django.utils import timezone
from django.utils.html import format_html 

from datetime import timedelta , date


class Tache(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    finie = models.BooleanField(default=False)
    date_echeance = models.DateTimeField(null=True)
    date_schedule = models.DateTimeField(null=True)

    def colored_date_echeance(self):
        now = timezone.now()
        for tache in Tache.objects.all():
            if tache.date_echeance:
                if tache.date_echeance > now:
                    return format_html('<span style="color: #FF0000;">{}</span>', tache.date_echeance)
                elif tache.date_echeance == now:
                    return format_html('<span style="color: #FFA500;">{}</span>', tache.date_echeance)
                else:
                    return format_html('<span style="color: #008000;">{}</span>', tache.date_echeance)
            else:
                return format_html('<span style="color: #FFA500;">{}</span>', "Pas de date d'échéance")
    colored_date_echeance.allow_tags = True

    def __str__(self):
        return self.titre