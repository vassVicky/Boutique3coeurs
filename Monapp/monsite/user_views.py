from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from django.contrib import messages
from .models import *
from datetime import datetime
from django.contrib.auth import authenticate , login , logout



class HomeView(View):
    template_index ='index.html'

    def get (self,request):
        if request.method == 'GET':
            value = request.GET.get('submit')
            if value == 'Deconnexion':
                logout(request)
                return redirect('home')

        return render(request,self.template_index)
        

class RegisterView(View):

    template_index ='register.html'
    

    def get (self,request):
        if request.method == 'GET':

           return render(request,self.template_index)
        

    def post(self,request):

        if request.method == 'POST':
            client = user = Client.objects.filter(username = request.POST.get('username'))
            if user.exists():
                messages.warning(request,"Cet utilisateur existe déjà")
            form = ClientForm(request.POST)
            if form.is_valid():
                user_profile = form.save(commit=False)
                date_format = "%Y-%m-%d"
                date_naissance = datetime.strptime(request.POST.get('datenaissance_client'), date_format)
                setattr(user_profile, 'datenaissance_client', date_naissance)
                user_profile.set_password(form.cleaned_data['password'])
                user_profile.save()
                messages.success(request, 'Compte a été crée avec succès')
                
                return redirect('register')  # Rediriger vers la page d'accueil après l'enregistrement
            else:
                    messages.error(request, 'Veuillez bien renseigner tous les champs requis')
            form = ClientForm()     
        return render(request,self.template_index, {'form': form})





class ConnexionView(View):

    template_index ='connexion.html'

    def get (self,request):
        if request.method == 'GET':

           return render(request,self.template_index)


    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Nom utilisateur ou mot de passe incorrect')
            context = {}
        return render(request, self.template_index, context)
    


class ContactView(View):
        
        template_index ='contact.html'

        def get (self,request):
            if request.method == 'GET':
                
                return render(request,self.template_index)
            

class AboutView(View):
        
        template_index ='about.html'

        def get (self,request):
            if request.method == 'GET':
                
                return render(request,self.template_index)
            


class ShopView(View):
        
        template_index ='shop.html'

        def get (self,request):
            if request.method == 'GET':
                     selected_value=request.GET.get('selected_value')
                     if selected_value != None:
                          produits = Produit.objects.filter(categorie=selected_value)
                     else:
                        produits = Produit.objects.all()
            context ={
                        'selected_value': selected_value,
                        'produits': produits
                    }
            return render(request,self.template_index , context)
        
        # def post(self, request):
        #     if request.method == 'POST':
        #         id_categorie = request.POST.get('selected')
        #         print(id_categorie)

        #         # password = request.POST.get('password')

        #         context = {}
        #     return render(request, self.template_index, context)



class CartView(View):
        
    template_index = 'cart.html'
    products = []

    def get(self, request):
        if request.method == 'GET':
            
            remove_value = request.GET.get('remove_produit')
            if remove_value != None:
                remove_produit = Produit.objects.get(id=remove_value)
                if remove_produit in  self.products:
                          self.products.remove(remove_produit)

            selected_value = request.GET.get('product_id')
            if selected_value is not None:
                produit = Produit.objects.get(id=selected_value)
                self.products.append(produit)
            
            

        context = {
            'produits': self.products,
            'products_nombre': len(self.products)
        }         
        
        return render(request, self.template_index, context)
            


        



class CheckoutView(View):
        
        template_index ='checkout.html'

        def get (self,request):
            if request.method == 'GET':
                
                return render(request,self.template_index)
            

class ThankyouView(View):
        
        template_index ='thankyou.html'

        def get (self,request):
            if request.method == 'GET':
                
                return render(request,self.template_index)
            

class ShopsingleView(View):
        
        template_index ='shop-single.html'

        def get (self,request):
            if request.method == 'GET':
                selected_value=request.GET.get('product_id')
                if selected_value != None:
                          produit = Produit.objects.get(id=selected_value)
                          print(produit)
                else:
                    messages.info(request, 'ce produit n\'existe pas')

            context ={
                        'selected_value': selected_value,
                        'produit': produit
                    }    
            return render(request,self.template_index, context)