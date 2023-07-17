from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _




class Client(AbstractUser):
    nom_client = models.CharField(max_length=255)
    prenom_client = models.CharField(max_length=255)
    datenaissance_client = models.DateField(null=True)
    email_client = models.EmailField() 
    adresse_client = models.CharField(max_length=255)
    numeroTel = models.CharField(max_length=15)

    def _str_(self):
        return self.username

    


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)
    qte_categorie = models.PositiveIntegerField() 

    def _str_(self):
        return self.nom_categorie
    


class Livraison(models.Model):
    ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    codepostal = models.CharField(max_length=10)
    date_livraison = models.DateTimeField()
   

    def _str_(self):
        return self.ville




class Commande(models.Model):

    STATUS_COMMANDE = (
        ('canceled', _('Annulé')),
        ('finished', _('Validé')),
    )
    
    date_commande = models.DateTimeField()
    qte_commande = models.PositiveIntegerField()
    statut_commande = models.CharField(max_length=255 , choices=STATUS_COMMANDE) 
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    livraison = models.ForeignKey(Livraison,on_delete=models.SET_NULL,null=True)
    
    def _str_(self):
        return str(self.statut_commande)


class Produit(models.Model):
    designation_produit = models.CharField(max_length=255)
    prix_produit = models.DecimalField(max_digits=10, decimal_places=2)
    details_produit = models.TextField()
    image_produit = models.ImageField(upload_to='produits/')
    qte_produit = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    commande= models.ForeignKey(Commande,on_delete=models.SET_NULL,null=True)


    def _str_(self):
        return self.designation_produit






class Operateur(models.Model):
   
    nom_operateur = models.CharField(max_length=255)


    def _str_(self):
        return self.nom_operateur



class Paiement(models.Model):

    STATUS_PAIEMENT = (
            ('canceled', _('Annulé')),
            ('paid', _('Payé')),
        )

    MODE_PAIEMENT = (
            ('e_pay', _('Paiement electronique')),
        )


    mode_paiement = models.CharField(max_length=255,choices=MODE_PAIEMENT)
    date_paiement = models.DateTimeField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=255,choices=STATUS_PAIEMENT)
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    operateur = models.OneToOneField(Operateur, on_delete=models.CASCADE)

    def _str_(self):
        return self.mode_paiement
    












