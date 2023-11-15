from django.contrib import admin
from .models import Billet
from .models import Character	
from .models import Equipement

admin.site.register(Billet)
admin.site.register(Character)
admin.site.register(Equipement)
