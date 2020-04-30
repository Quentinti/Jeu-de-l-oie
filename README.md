# Projet du jeu de l'oie | ISN 2019

![Plateau du jeu de l'oie](http://image.noelshack.com/fichiers/2020/18/4/1588281134-plateau.jpg)

***Plusieurs joueurs sur un même plateau doivent s’affronter pour parvenir au plus vite à la case finale. Attention cependant, certaines de ces cases sont des pièges !***

## Sommaire

1. Pourquoi ce projet ?
2. Les règles du jeu de l'oie !
3. Captures d'écrans clés
4. Fonctionnalités
5. Dépendances
6. Utilisation du programme
7. Crédits

## Pourquoi ce projet ?

Dans le cadre de la discipline ISN, nous devions faire un projet durant l’année scolaire pour le baccalauréat.

Le but principal du projet était de pouvoir faire se **déplacer des pions sur un plateau**. De plus, leur déplacement devait correspondre aux règles imposées par le jeu de l’oie.

Pour cela on a utilisé le langage de programmation **Python**. Il est relativement simple à comprendre et puissant. De plus la documentation est très complète, on a résolu beaucoup de nos problèmes grâce aux sites **[Stack Overflow](https://stackoverflow.com/)** et **[OpenClassrooms](https://openclassrooms.com/fr/)**. Nous avons largement utilisé le module **Tkinter de Python pour la partie graphique**.

## Les règles du jeu de l'oie ! 

- **Au commencement** de la partie, si l’un des joueurs fait **9** par **6** et **3**, il doit avancer son pion immédiatement au nombre **53**. S’il fait **9** par **4** et **5**, il ira au nombre **26**.
- Si lors de la partie, le joueur tombe sur une **oie**, il avance de nouveau du nombre de points réalisés.
- Si un joueur fait **6**, il doit se rendre sur la case **12**.
- Le joueur qui tombe sur la case **19** correspondant à un **hôtel** devra passer son tour durant **2** tours.
- Le joueur qui tombe sur la case **31** correspondant au puits attendra qu’un autre joueur arrive au même numéro et **prendra sa place**.
- Celui qui tombe sur la case **42** correspondant au labyrinthe retournera obligatoirement à la case **30**.
- La case **52** étant la **prison**, le joueur piégé à cette case attendra qu’un autre joueur s’y rende pour repartir.
- Le joueur qui va sur la case **58** correspondant à la case **Tête de mort** recommencera la partie depuis le début.
- Celui qui est rejoint par un autre joueur sur la **même case** devra se rendre sur la case ou l’autre joueur se situait **avant de jouer**.
- Pour gagner, le joueur doit tomber **pile sur la case 63**. Si ce n’est pas le cas, il devra **reculer** du nombre de cases en trop.

*Règle ajoutée : le joueur à la case ***51*** qui fait ***8***, avancera de seulement ***4*** cases. Sans cela, son déplacement serait ***infini*** répété par l’oie de la case 59.*


> NB : Ces règles ne sont pas rédigées par nos propres soins !
> Règles trouvables à ce **[lien](https://www.regles-de-jeux.com/regle-du-jeu-de-l-oie/)**

## Captures d'écrans clés


![Partie en cours](http://image.noelshack.com/fichiers/2020/18/4/1588282636-partie-en-cours.png)

*Partie en cours du jeu de l'oie...*

![Parametres](http://image.noelshack.com/fichiers/2020/18/4/1588282774-parametres.png)

*Les options du jeu en mode sombre, où la langue sélectionnée est l’italien et les paramètres sonores sont modifiés*

![Chargement](http://image.noelshack.com/fichiers/2020/18/4/1588282853-chargement.png)

*L’écran de chargement du jeu. Il s’agit en réalité d’un temps d’attente prédéfini, l’effet est purement esthétique.*

## Fonctionnalités

- **Choix du nombre de joueurs de 2 à 6**
- **Déplacement en temps réel des pions sur le plateau**
- **Options disponibles configurables en temps réel**
    - **Système de langue avec +100 langues !**
    - **Curseurs de réglage du son**
    - **Bouton d'activation/désactivation du son**
    - **Mode sombre**
- **Menu d'aide avec les règles du jeu**
- **Menu principal**
- **Classement des joueurs**
- **Bruitages sonores et musique**
- **Écran de chargement**

## Dépendances

Pour que ce programme **fonctionne correctement**, certaines dépendances sont **indispensables** !

```python
    from tkinter import *
    from PIL import ImageTk, Image, ImageDraw
    import shutil
    import os
    import contextlib
    import pygame
```

- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** *pour l'interface graphique*
- **[PIL / Pillow](https://pillow.readthedocs.io/en/stable/)** *pour la manipulation des images*
- **[Shutil](https://docs.python.org/3/library/shutil.html)** *pour la suppression du dossier temporaire*
- **[OS](https://docs.python.org/3/library/os.html)** *pour la création du dossier temporaire*
- **[Contextlib](https://docs.python.org/3/library/contextlib.html)** *pour l'importation de Pygame*
- **[pygame](https://www.pygame.org)** *pour l'utilisation du son*

> Nous avons utilisé Tkinter au lieu de pygame car cela était imposer par le sujet 


Utilisez le gestionnaire de dépendances [pip](https://pip.pypa.io/en/stable/) pour les installer.

```bash
pip install pygame
pip install tkinter
pip install pillow
pip install shutil
pip install os
pip install contextlib
```

## Utilisation du programme

## Crédits
