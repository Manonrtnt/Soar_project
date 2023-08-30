# Soar_project
Système d'Observation et d'Analyse du Réseau

## Présentation du Projet SOAR : Système d'Observation et d'Analyse du Réseau

Le Projet SOAR (Système d'Observation et d'Analyse du Réseau) est une application conçue pour surveiller, analyser et capturer les paquets réseau. 

## Informations sur la Version du Projet
- Framework utilisé : Django 4.2

## Objectifs du Projet
Le projet SOAR a pour objectifs principaux :
- Offrir une interface conviviale pour la surveillance et l'analyse du trafic réseau.
- Faciliter la capture de paquets réseau pour une analyse approfondie.
- Fournir une plateforme sécurisée pour l'exécution de scripts Scapy avec des privilèges sudo.

## GIT
### Ajouter le Projet au Gestionnaire de Versions (Git)
Lien du dépôt git :
```
[<lien du repository>](https://github.com/Manonrtnt/Soar_project.git)
```

Commande pour cloner le projet :
```
git clone https://github.com/Manonrtnt/Soar_project.git
```

## Créer un Utilisateur Administrateur
- Un compte administrateur est nécessaire pour accéder aux formulaire et lancer une demande de capture. 
   
1. Ouvrez un terminal et assurez-vous d'être dans le répertoire racine de votre projet Django où se trouve le fichier `manage.py`.

2. Utilisez la commande suivante pour créer un superutilisateur :
   
   ```bash
   python3 manage.py createsuperuser
   ```

3. Suivez les invites pour saisir un nom d'utilisateur, une adresse e-mail et un mot de passe pour l'administrateur.

---
Note : Une fois le superutilisateur créé, vous pouvez l'utiliser pour vous connecter à la partie d'administration de votre site, accéder aux formulaire et lancer une demande de capture.

## Gestion des Droits Utilisateur
### Ajouter des Droits Sudo pour l'Utilisateur Django
Pour permettre à l'utilisateur Django d'exécuter des scripts Scapy avec des privilèges sudo sans mot de passe :
1. Ouvrez le fichier sudoers en éditant les droits :
   ```
   sudo visudo
   ```

2. Ajoutez la ligne suivante pour autoriser l'utilisateur spécifié (dans cet exemple, "utilisateur") à exécuter Python 3 avec des privilèges sudo, ainsi que le chemin complet du dossier de scripts :
   ```
   <utilisateur> ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/osboxes/soar_project/script_scapy/capture_option1_paquet.py
   <utilisateur> ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/osboxes/soar_project/script_scapy/capture_option2_couche_ethernet.py
   <utilisateur> ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/osboxes/soar_project/script_scapy/capture_option3_couche_ip.py
   <utilisateur> ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/osboxes/soar_project/script_scapy/capture_option4_couche_tcp.py

   ```
   Note : remplacer utilsiateur par l'utilsiateur exécutant le serveur
   Note : Assurez-vous que le chemin vers le dossier de scripts est correct.

## Accéder au Site
Pour accéder au site depuis une machine distante :
- Utilisez la commande `ip a` pour récupérer l'adresse IP privée de l'hôte.
### Exécution du Serveur
1. Pour autoriser l'accès à votre application depuis d'autres machines, modifiez le fichier `soar_project/settings.py` en ajoutant votre adresse IP à la liste `ALLOWED_HOSTS` :
   ```
   ALLOWED_HOSTS = ['192.168.56.12', 'localhost', '127.0.0.1', 'votre adresse IP']
   ```
   
2. Naviguez vers le dossier du projet dans un terminal :
   ```
   cd soar_project/
   ```

3. Lancez le serveur Django en utilisant la commande suivante (permettant aux autres machines de se connecter) :
   ```
   python3 manage.py runserver 0.0.0.0:8000
   ```
   Note : L'adresse `0.0.0.0` signifie que le serveur écoute sur toutes les interfaces réseau.

   Pour plus d'informations sur la commande `runserver`, consultez [cette documentation](https://docs.djangoproject.com/en/4.2/ref/django-admin/#runserver).

### Accès à l'adresse du projet
- url d'accès : <adresseip>:8000/soar_project

### Connexion
Pour accéder au formulaire, connectez-vous avec vos identifiants administrateur (cf partie concernant .

## Capture de Paquets
### Test de Capture
Pour tester une capture de paquets :
1. Ouvrez un nouveau terminal.

2. Exécutez la commande `ping` pour générer du trafic réseau :
   ```
   ping 8.8.8.8
   ```
3. Ouvrir l'application : adresse

4. Se connecter 

5. Lancer une demande depuis le formulaire

6. Visualiser les informations sur le terminal et découvrer le fichier crée depuis le dossier : soar_project/capture/
---

N'oubliez pas d'ajuster les chemins de fichiers, les adresses IP et autres détails selon votre configuration. Cette documentation devrait offrir un aperçu complet de l'installation, de l'utilisation et de la configuration de votre projet SOAR.
