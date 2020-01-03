from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from backoffice.models import *
import hashlib, binascii, os
from django.contrib import messages
from django.template.response import TemplateResponse

def home(request):
    return HttpResponse("Bonjour monde!")

# deconnexion
class LogoutView(TemplateView):

  template_name = 'front/index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)

# Page de connexion
class LoginView(TemplateView):
  template_name = 'front/index.html'

  def get(self, request, **kwargs):
    print("index")
    return render(request, self.template_name)

  def post(self, request, **kwargs) :
    # paramètres
    login = request.POST.get('username', False)
    password = request.POST.get('password', False)

    #verifications
    try:
      # account exist
      account_exist = Account.objects.filter(pseudo = login).count()
      if(account_exist != 1):
        raise ValueError("Le pseudo n'existe pas.")

      # password
      account = Account.objects.get(pseudo = login)
      password_is_ok = verify_password(account.password, password)
      if(password_is_ok == False):
        raise ValueError("Le mot de passe n'est pas correcte.")

      request.session['pseudo'] = login
      return HttpResponseRedirect( "data" )

    # retourner l'erreur
    except ValueError as error:
        print(error)
        messages.warning(request, error.args[0])
        return render(request, 'front/index.html')

# créer un compte
class RegisterView(TemplateView) :
  template_name = 'front/register.html'

  def get(self, request, **kwargs):
    return render(request, 'front/register.html')
    #return HttpResponse("register !")

  def post(self, request, *args, **kwargs):

    # paramètres
    login = request.POST.get('username', False)
    password = request.POST.get('password', False)

    #verifications
    try:
      # verif login
      shortLogin = login.replace(' ',"")
      if shortLogin == "":
          print("Pseudo invalide")
          raise ValueError("Vous devez entrer un login !")
      
      # verif password
      shortPassword = password.replace(' ',"")
      if len(shortPassword) < 4:
          print("Mot de passe invalide")
          raise ValueError("Le mot de passe doit contenir au moins 4 caractères !")
      
      account_exist = Account.objects.filter(pseudo = login).count()

      # verif if login is available
      if(account_exist > 0) :
         raise ValueError("Le pseudo existe déjà : \""+login+"\".")
      
      # save account
      account = Account()
      account.pseudo = login
      account.password = hash_password(password)
      account.save()

      messages.success(request, "Le compte à été créé.")
      return render(request, 'front/index.html')

    # retourner l'erreur
    except ValueError as error:
        print(error)
        messages.warning(request, error.args[0])
        return render(request, 'front/register.html')

# voir les données
class DataView(TemplateView) :
  template_name = 'front/data.html'

  def get(self, request, **kwargs):

    # si l'utilisateur n'est pas connecté
    if ('pseudo' in request.session) == False:
      return HttpResponseRedirect( settings.LOGIN_URL ) 

    args = {}
    args['infos'] = data.objects.all()  

    return TemplateResponse(request, 'front/data.html', args)

  def post(self, request, *args, **kwargs):

    # si l'utilisateur n'est pas connecté
    if ('pseudo' in request.session) == False:
      return HttpResponseRedirect( settings.LOGIN_URL ) 

    #variable
    new_data = request.POST.get('data', "")

    #verifications
    try:
      # verif login
      if new_data == "":
          raise ValueError("Vous devez ecrire quelque chose!")
      
      # save account
      info = data()
      info.texte = new_data
      info.save()

      return HttpResponseRedirect( "data" ) 

    # retourner l'erreur
    except ValueError as error:
      messages.warning(request, error.args[0])
      args = {}
      args['infos'] = data.objects.all()  
      return TemplateResponse(request, 'front/data.html', args)

# hash_password : hash password with salt 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# verify_password : verify password with hash password
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password