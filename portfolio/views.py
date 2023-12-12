from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from portfolio.entity.utilisateur import Utilisateur
from django.core.mail import send_mail

from portfolio.forms import UtilisateurForms

# Create your views here.
    

@login_required
def detail_utilisateur(request):
    if request.method=='POST':
        ajout = UtilisateurForms(request.POST)
        if ajout.is_valid():
            nom=ajout.cleaned_data.get('nom')
            poste=ajout.cleaned_data.get('poste')
            observation=ajout.cleaned_data.get('observation')
            mail=ajout.cleaned_data.get('mail')
            mdp=ajout.cleaned_data.get('mdp')
            Utilisateur.objects.create(nom=nom,poste=poste,observation=observation,mail=mail,mdp=mdp)
        ajout = UtilisateurForms()
    else:
        ajout = UtilisateurForms()
    utilisateurs = Utilisateur.objects.all()
    return render(request,'formulaire.html',{'utilisateurs':utilisateurs,'form':ajout})

def accueil(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('contact.html')
    context={}
    return HttpResponse(template.render(context,request))

def loisir(request):
    template = loader.get_template('loisir.html')
    context={}
    return HttpResponse(template.render(context,request))

def realisation(request):
    template = loader.get_template('realisation.html')
    context={}
    return HttpResponse(template.render(context,request))

def competence(request):
    template = loader.get_template('competence.html')
    context={}
    return HttpResponse(template.render(context,request))

def formulaire(request):
    template = loader.get_template('formulaire.html')
    if request.method=='POST':
        ajout = UtilisateurForms(request.POST)
        if ajout.is_valid():
            nom=ajout.cleaned_data.get('nom')
            poste=ajout.cleaned_data.get('poste')
            observation=ajout.cleaned_data.get('observation')
            mail=ajout.cleaned_data.get('mail')
            mdp=ajout.cleaned_data.get('mdp')
            Utilisateur.objects.create(nom=nom,poste=poste,observation=observation,mail=mail,mdp=mdp)
        ajout = UtilisateurForms()
    else:
        ajout = UtilisateurForms()
    utilisateurs = Utilisateur.objects.all()
    context={'utilisateurs':utilisateurs,'form':ajout}
    return HttpResponse(template.render(context,request))



# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )