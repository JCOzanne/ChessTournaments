# ChessTournaments
Ce projet est une application en ligne de commande pour gérer des tournois d'échecs. Elle permet de créer des tournois, d'ajouter des joueurs, de gérer les rondes et de générer des rapports sur les tournois et les joueurs.

## Fonctionnalités

- **Créer un tournoi** : Créez un nouveau tournoi avec un nom, un lieu, des dates de début et de fin, et une description.
- **Ajouter des joueurs** : Ajoutez des joueurs à un tournoi en fournissant leur nom, prénom, date de naissance et identifiant national d'échecs.
- **Gérer les rondes** : Gérez les différentes rondes d'un tournoi, y compris la génération automatique des matchs et la saisie des résultats.
- **Générer des rapports** : Affichez des rapports sur les joueurs, les tournois, les matchs, et les rondes.

## Structure du Projet

Le projet est organisé en plusieurs modules pour une meilleure gestion du code :

- **models** : Contient les classes principales comme `Player`, `Match`, `Round`, et `Tournament`.
- **views** : Contient les fonctions d'affichage pour les différentes interfaces utilisateur.
- **controllers** : Contient les fonctions de contrôle pour gérer la logique du programme.
- **utils** : Contient les utilitaires pour la gestion des données, comme la sauvegarde et le chargement des joueurs et des tournois.

## Prérequis

- Python 3.12
- Les bibliothèques Python mentionnées dans requirements.txt

$ pip install -r requirements.txt

## Installation

1. **Cloner le dépôt :**  
$ git clone git@github.com:JCOzanne/ChessTournaments.git


2. **Créer et activer l'environnement virtuel**

- sur windows  
$ cd ChessTournaments  
$ python -m venv env  
$ ~env\scripts\activate  


- sur MacOS / Linux  
$ cd ChessTournaments  
$ python3 -m venv env 
$ source/env/bin/activate

3- **Lancer le programme**

- sur windows :  
$ python main.py  


- sur Mac OS / Linux :  
$ python3 main.py  

4- **Utilisation**

Lorsque vous lancer le programme, le menu principal s'affiche et vous propose :  

1- créer un tournoi  
2- générer un rapport  
3- quitter

**Le menu 1** permet de créer un nouveau tournoi avec un nom, un lieu et une date et un nombre de rondes.  
Le programme vous propose d'ajouter les joueurs du tournoi avec leur nom, prénom, date de naissance et numéro national d'échecs.  
Lorsque les joueurs ont été renseignés, vous pouvez nommer la première ronde. A ce moment, la date et l'heure de la première ronde s'affiche.
Vous pouvez alors renseigner le résultats des matchs que le programme vous propose.
Lorsque les matchs ont été renseignés, le programme vous propose de passer à la ronde suivante, marque la date et l'heure de la fon de ronde, et ainsi de suite.  

**Le menu 2** permet de générer les rapports:  
- liste de tous les joueurs par ordre alphabétique,
- liste de tous les tournois,
- nom et date d'un tournoi donné,
- liste des joueurs d'un tournoi donné par ordre alphabétique,
- liste de toutes les rondes et de tous les matchs d'un tournoi donné
- retour au menu principal.

5- **Rapport Flake8**

Un rapport flake8 a été généré avec la commande :  
$ flake8 controllers utils models views main.py --max-line=119 --format=html --htmldir=flake8-report



