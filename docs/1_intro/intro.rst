Introduction
============

Dans ce tutoriel tu vas apprendre à programmer dans un langage qui s'appelle **Python**.
Tu vas programmer les déplacements d'une tortue. Voici à quoi ça va ressembler.

.. image:: epfl1.png

:download:`epfl1.py <epfl1.py>`

Cette tortue laisse une trace qui te permet de faire des dessins.
Mais tout d'abord tu dois télécharger un outil pour programmer.

Installer un éditeur
--------------------

Vas sur le site https://thonny.org
et télécharge l'application **Thonny**.

C'est un éditeur de programme qui te permet

- **écrire** un programme
- **executer** ce programme
- **afficher** le résultat

Dans Thonny tu as trois régions

#. les **boutons** pour *Créer, Ouvrir, Sauvegarder, Executer* un programme
#. la partie **éditeur** pour écrire un programme entier
#. la **console** pour executer des commandes courtes (Shell)

.. image:: thonny.png


Les premiers pas
----------------

Dans la console (ou Shell) tu peux directement entrer des expressions courtes que Python peut évaluer.
Après les 3 chevrons (>>>) tu peux écrire cette addition::

    >>> 1 + 2
    3

Tu peux aussi essayer cette muliplication::

    >>> 12 + 13
    156

Python n'est pas limité dans le nombre de chiffres qu'un calcul peut produire.
Voici une puissance de deux nombres qui donne un résultat qui s'étale sur 5 lignes::

    >>> 123 ** 123
    11437436793461719009988029522806627674621807845185022977588797
    50523695047856668964466065683652015421696499747277306288423453
    43196581134895919942820874449837212099476648958359023796078549
    04194900780722062535652692672966406484668575838280370710076674
    0220839267



Dessiner avec une tortue
------------------------

Par la suite nous allons utiliser le module ``turtle``.
Ce module te permet de déplacer une tortue sur l'écran, 
à l'aide des commandes que tu programmes.

Pour pouvoir utiliser ce module, tu dois l'importer au début du programme::

    >>> import turtle

Ensuite tu peux donner un ordre à ta tortue::

    >>> turtle.forward(100)

Cette commande fait avancer la tortue de 100 pixels. 
Une commande pour contrôler la tortue a la forme suivante:

- un premier mot ``turtle.`` (avec un point)
- une commande (forward, backward, left, right, etc.)
- des parenthèses ``( )``
- un argument numériques (distance, angle)

Pour faire faire reculer la tortue de 200 pixels écris ceci::

    >>> turtle.backward(200)

Pour faire tourner la tortue de 90 degrès vers laisse gauche::

    >>> turtle.left(90)

Pour faire tourner la tortue de 45 degrès vers la droite::

    >>> turtle.right(45)

La console est un outil très pratique. 
A n'importe quel moment tu peux facilement tester des commandes.

Remonter dans l'historique
--------------------------

Toutes les commandes que tu as entrées dans la console pendant une session,
tu peux facilement les retrouver, les modifier et les réutiliser.

.. image:: arrows.png

Il suffit d'utiliser les flèches **haut** et **bas** pour te balader 
dans le historique de tes commandes.

Essaye, c'est très pratique.


Ecrire un programme
-------------------

Tous ces commandes que tu peux écrire directement dans la console, 
tu peux aussi les mettre dans un **programme** (qu'on appelle **script**).

Un programme n'est rien d'autre qu'une *liste de commandes qui dit à la tortue comment bouger*.
Une fois le programme terminé, tu peux l'executer à l'aide du bouton vert **Executer**.
A ce moment Thonny te demande de donner un nom à ton programme.

Le programme suivant dessine un triangle. 
Essaye de le programmer!

.. image:: triangle.png

.. literalinclude:: triangle.py

:download:`triangle.py <triangle.py>`

Tu remarque l'instruction ``turtle.done()`` sur la dernière ligne.
Elle est nécessaire avec certains éditeurs de code pour garder la fenêtre ouverte.
Avec Thonny cette ligne n'est pas nécessaire, et tu peux l'ignorer.


Dessiner une maison
-------------------

En utilisant des angles de 45 et 90 degrees, tu peux dessiner une maison.

.. image:: house.png

.. literalinclude:: house.py

:download:`house.py <house.py>`


Ajouter une porte
-----------------

Tu peux ajouter une porte en dessinant encore un rectangle.

.. image:: house2.png

.. literalinclude:: house2.py

:download:`house2.py <house2.py>`


Erreurs fréquentes
------------------

Si tu fais une erreur avec le nom du module, par exemple *turtel* au lieu de *turtle*,
tu obtiens une erreur de type ``ModuleNotFoundError``::

    >>> import turtel
    ModuleNotFoundError: No module named 'turtel'

Si tu oublies de donner un argument à une fonction, 
par exemple si tu oublies de mettre und distance pour la fonction *forward()*, 
tu obtiens une erreur de type ``TypeError``::

    >>> turtle.forward()
    TypeError: forward() missing 1 required positional argument: 'distance'

Si tu fais une erreur dans le nom d'une fonction, par exemple *foreward* au lieu de *forward*, 
tu obtiens une erreur de type ``AttributeError``::

    >>> turtle.foreward(100)
    AttributeError: module 'turtle' has no attribute 'foreward'

**Conseil** 

* Lis la dernière ligne du message d'erreur
* Essaie de trouver l'erreur dans ton code
* Corrige l'erreur et relance ton programme

Raccourcir le code
------------------

Si tu veux raccourcir ton code, 
tu peut importer toutes les commandes dans l'espace de ta session avec le symbole ``*`` ::

    >>> from turtle import *

Ensuite tu dois créer un objet ``Screen()`` qui ouvre une fenêtre::

    >>> Screen()
    <turtle._Screen object at 0x1063f68d0>

Maintenant tu peux directement utiliser les fonctions, sans les précéder de ``turtle.`` ::

    >>> forward(100)
    >>> left(45)
    >>> forward(100)

Si tu veux écrire tes commandes encore plus courtes, 
tu peux utiliser les raccourcis à deux lettres: 
``fd`` (forward), ``bk`` (back), ``lt`` (left) et ``rt`` (right) ::

    >>> fd(100)
    >>> lt(45)
    >>> fd(100)
    >>> rt(90)
    >>> fd(100)
    >>> bk(200)
    