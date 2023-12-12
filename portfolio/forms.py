from django import forms
from django.shortcuts import render
from portfolio.entity.utilisateur import *

class UtilisateurForms(forms.Form):
    nom = forms.CharField(max_length = 150,error_messages={"required":"champs obligatoire"})
    post = forms.CharField(max_length = 150,error_messages={"required":"champs obligatoire"})
    observation = forms.CharField(max_length = 150,error_messages={"required":"champs obligatoire"})
    mail = forms.CharField(max_length = 150,error_messages={"required":"champs obligatoire"})
    mdp = forms.CharField(max_length=15,error_messages={"required":"champs obligatoire"})


            
            