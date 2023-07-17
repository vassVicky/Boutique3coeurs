from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Categorie)
admin.site.register(Paiement)
admin.site.register(Operateur)
admin.site.register(Livraison)
admin.site.register(Produit)