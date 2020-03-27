L'aléatoire
===========

L'aléatoire est ce qui relève du hasard. 
Quand on roule un dé, son résultat est aléatoire.

Dans des jeux ou des animations, il est souvent nécessaire de pouvoir calculer des valeurs aléatores. 
Le module ``random`` permet de trouver des valeurs aléatoires.

Partant du centre, la tortue visite les 13 sections de l'EPFL 
qui se trouvent tous à des positions aléatoires sur cette carte.

.. image:: epfl4.png

:download:`epfl4.py <epfl4.py>`

Position aléatoire
------------------

Pour pouvoir utiliser des fonctions aléatoirs nous devons d'abord importer le module ``random``::

    import random

La fonction ``random.randint(-100, 100)`` retourne une valeur aléatoire 
qui se situe entre les deux valeurs -100 et 100.  
Pour obtenir une position aléatoire, nous devons calculer deux valeurs, x et y.

.. image:: random1.png

.. literalinclude:: random1.py
   :lines: 2-

:download:`random1.py <random1.py>`


Angle aléatoire
---------------

Pour simuler la marche aléatoire d'une fourmi, nous pouvons garder la distance de chaque pas
constante, et choisir l'angle du changement de direction à chaque itération comme ceci::

    angle = random.randint(-90, 90)

.. image:: random2.png

.. literalinclude:: random2.py
   :lines: 2-

:download:`random2.py <random2.py>`


Taille aléatoire
----------------

Ci-dessous la tortue va à une position (x, y) aléatoire et choisit une taille aléatoire 
dans l'intervalle [10, 50] pour dessiner un cercle::

    size = random.randint(10, 50)  
    goto(x, y)
    dot(size)

.. image:: random3.png

.. literalinclude:: random3.py
   :lines: 2-

:download:`random3.py <random3.py>`


Couleur aléatoire
-----------------

La fonction ``random.choice(list)`` permet de choisir un élément dans une liste. 
Il faut d'abord définir une liste::

    colors = ('red', 'blue', 'green', 'violet', 'yellow', 'cyan', 'orange', 'magenta')

Ensuite un élément aléatoire est choisi dans cette liste et utilisé comme nouvelle
couleur pour la tortue::

    color = random.choice(colors)
    pencolor(color)

.. image:: random4.png

.. literalinclude:: random4.py
   :lines: 2-

:download:`random4.py <random4.py>`

