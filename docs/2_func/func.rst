La fonction
===========

Avec les 4 fonctions *forward, backward, left, right* tu peux tout dessiner.
Par contre, dès que ton dessin devient un peu plus complexe ton programme 

- comporte beaucoup de répétitions,
- est difficile à lire (et comprendre).

.. image:: flower.png

La solution est d'utiliser une **fonction** qui permet de

- mettre un bout du code à part
- donner un **nom** à ce code
- **réutiliser** ce code autant de fois que tu veux

Les deux fleurs ci-dessus ont été dessinées à l'aide d'une fonction qu'on a appelé ``flower()``.

Définir une fonction
--------------------

Tout d'abord nous devons définir la fonction. Une définition de fonction est constituée :

- du **mot-clé** ``def`` (qui veut dire définition)
- du **nom** de la fonction
- de **parenthèses** ``()``
- du signe **deux-points** ``:``
- du **corps** de la fonction contenant le code.

Voici, par example, la définition de la fonction **triangle**::

    def triangle():
        forward(100)
        left(120)
        forward(100)
        left(120)
        forward(100)
        left(120)
        forward(100)

Pour indiquer les commandes qui font partie de cette fonction,
tu dois les décaler vers la droite. 
On appelle ça **indenter** le corps de la fonction. 

Cette **indentation** est un point important qui distingue Python d'autres langages de programmation.
L'indentation te montre visuellement ce qui fait partie du corps de la fonction.

Quand une expression en Python se termine avec le signe **deux-points**, 
la ligne suivante est automatiquement indenté de 4 espaces.

La définition d'une fonction toute seule ne vas rien dessiner.
Tu dois **appeler** la fonction dans ton programme pour exécuter son code. 
Pour appeler une fonction dans ton programme tu dois écrire:

- le **nom** de la fonction
- des **parenthèses** ``()``

Voici la fonction ``triangle()`` appelée trois fois::

    triangle()
    triangle()
    triangle()

.. image:: func1.png

.. literalinclude:: func1.py
   :lines: 2-

:download:`func1.py <func1.py>`

Tu dois d'abord définir une fonction avant que tu puisse l'appeler.
C'est pour cela qu'on met les définitions de fonction au début du programme.
Une fois définie, tu peux appeler une fonction autant de fois que tu veux.

Appeler une fonction dans une fonction
--------------------------------------

Une fonction peut appeler une autre fonction. 
Pour dessiner un carré, nous pouvons d'abord définir une fonction ``side`` qui dessine
juste un côté et tourne de 90 degrées::

    def side():
        forward(100)
        left(90)

Ensuite la fonction ``square()`` appelle 4 fois cette fonction::

    def square():
        side()
        side()
        side()
        side()
        forward(100)

Et finalement tu peux appeler 3 fois la fonction ``square``::

    square()
    square()
    square()

.. image:: func2.png

.. literalinclude:: func2.py
   :lines: 2-

:download:`func2.py <func2.py>`

Dessiner des maisons
--------------------

Tu peux reprendre le dessin de la maison vu dans l'introduction. 
Nous allons le définir comme fonction. En plus, nous allons ajouter un remplissage.
Ceci va nous permettre de dessiner plusieurs maisons à des positions et dans les couleurs que tu veux.

Voici un exemple:

.. image:: house.png

.. literalinclude:: house.py
   :lines: 2-

:download:`house.py <house.py>`


Dessiner des fleurs
-------------------

Tu peux utiliser deux arcs de cercle de 90 degrés pour dessiner un pétale::

    def petal():
        begin_fill()
        circle(50, 90)
        left(90)
        circle(50, 90)
        end_fill()
        left(18)

Ensuite tu peux combiner 5 pétales pour dessiner une fleur.

.. image:: flower.png

.. literalinclude:: flower.py
   :lines: 2-

:download:`flower.py <flower.py>`
