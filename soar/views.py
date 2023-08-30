from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import FormView
from django.views import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from scapy.all import sniff, Ether, IP, TCP
import os
import subprocess

from .form import CaptureRequestForm
from .models import CaptureRequest


def IndexView(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class CaptureRequestView(FormView):
    template_name = 'index.html'
    form_class = CaptureRequestForm
    success_url = reverse_lazy('capture_request_success')

    # Check les droits de l'utilisateur en cours
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        # Vérification des privilèges administratifs
        if os.geteuid() != 0:
            print("Ce script doit être exécuté avec des privilèges administratifs (sudo).")
            # exit(1)
        return super().dispatch(request, *args, **kwargs)

    #    def form_valid(self, form):
    #        form.save()
    #        
    #        captured_packets = ""
    #    
    #        # Récupérer le choix de l'utilisateur
    #        choice = form.cleaned_data['requestCode']
    #        
    #        # Débogage
    #        print(f"Choice selected: {choice}")
    #    
    #        # Exécution du script Scapy via subprocess avec privilèges
    #        try:
    #            script_path = '/home/osboxes/soar_project/script_scapy/capture_packets.py'
    #            print(f"Executing script: {script_path}")
    #            result = subprocess.run(['sudo', 'python3', script_path])
    #
    #            print(f"try, {captured_packets}")
    #        except Exception as e:
    #            captured_packets = [f"Erreur : {e}"]
    #            print(f"catch, {captured_packets}")
    #    
    #        context = self.get_context_data(form=form, captured_packets=captured_packets)
    #        
    #        # Redirection vers la page de succès
    #        return super().form_valid(form)

    def form_valid(self, form):
        form.save()

        # Récupérer le choix de l'utilisateur
        choice = form.cleaned_data['requestCode']

        # Débogage
        print(f"Choice selected: {choice}")

        # Sélectionner le chemin du script en fonction du choix
        # Option 1 : Capturer tous les paquets
        if choice == 1:
            script_path = '/home/osboxes/soar_project/script_scapy/capture_option1_paquet.py'
        # Option 2 : Capturer les paquets de la couche Ethernet
        elif choice == 2:
            script_path = '/home/osboxes/soar_project/script_scapy/capture_option2_couche_ethernet.py'
        # Option 3 : Capturer les paquets de la couche IP
        elif choice == 3:
            script_path = '/home/osboxes/soar_project/script_scapy/capture_option3_couche_ip.py'
        # Option 4 : Capturer les paquets de la couche TCP
        elif choice == 4:
            script_path = '/home/osboxes/soar_project/script_scapy/capture_option4_couche_tcp.py'
        else:
            # Si le choix n'est pas reconnu, affichez une erreur
            context = self.get_context_data(form=form, captured_packets=["Erreur : Choix non reconnu"])
            print(f"Choix non ok")
            return self.render_to_response(context)

        # Exécution du script Scapy via subprocess avec privilèges
        try:
            print(f"Executing script: {script_path}")
            subprocess.run(['sudo', 'python3', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing script: {e}")

        context = self.get_context_data(form=form, captured_packets=[])

        # Redirection vers la page de succès
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class LoginView(FormView):
    template_name = 'index.html'
    form_class = AuthenticationForm
    success_url = '../'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class CaptureRequestSuccessView(View):
    template_name = 'capture_request_success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)