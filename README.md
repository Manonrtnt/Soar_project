# Soar_project
Système d'Observation et d'Analyse du Réseau

## Présentation du Projet SOAR : Système d'Observation et d'Analyse du Réseau

Le Projet SOAR (Système d'Observation et d'Analyse du Réseau) est une application conçue pour surveiller, analyser et capturer les paquets réseau. 

## Objectifs du Projet
Le projet SOAR a pour objectifs principaux :
- Offrir une interface conviviale pour la surveillance et l'analyse du trafic réseau.
- Faciliter la capture de paquets réseau pour une analyse approfondie.
- Fournir une plateforme sécurisée pour l'exécution de scripts Scapy avec des privilèges sudo.

## GIT
### Ajouter le Projet au Gestionnaire de Versions (Git)
Lien du dépôt git :
```
<lien du repository>
```

Commande pour cloner le projet :
```
git clone <lien du repository>
```

## Informations sur la Version du Projet
- Framework utilisé : Django 4.2

## Exécution du Serveur
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

### Accéder au Site
Pour accéder au site depuis une machine distante :
- Utilisez la commande `ip a` pour récupérer l'adresse IP privée de l'hôte.

## Connexion
Pour accéder au formulaire, connectez-vous avec vos identifiants.

## Gestion des Droits Utilisateur
### Ajouter des Droits Sudo pour l'Utilisateur Django
Pour permettre à l'utilisateur Django d'exécuter des scripts Scapy avec des privilèges sudo sans mot de passe :
1. Ouvrez le fichier sudoers en éditant les droits :
   ```
   sudo visudo
   ```

2. Ajoutez la ligne suivante pour autoriser l'utilisateur spécifié (dans cet exemple, "utilisateur") à exécuter Python 3 avec des privilèges sudo, ainsi que le chemin complet du dossier de scripts :
   ```
   <utilisateur> ALL=(ALL) NOPASSWD: /usr/bin/python3 /chemin/complet/vers/dossier_scripts/*
   ```
   Note : remplacer utilsiateur par l'utilsiateur exécutant le serveur
   Note : Assurez-vous que le chemin vers le dossier de scripts est correct.

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
