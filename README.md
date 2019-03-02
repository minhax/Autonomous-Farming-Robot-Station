# Enjambeur_Agricole

# Sommaire

I. [Introduction](#Introduction)

II. [Objectifs du projet](#Objectifs)

III. [Architecture générale](#Archi G)

IV. [Architecture Matérielle](#Archi M)

V. [Architecture Logicielle](#Archi L)

VI. [Lancement](#Lancement)

## Introduction <a id="Introduction"></a>
Dans le cadre de la transition écologique de l’agriculture française et européenne vers une agriculture responsable dite « biologique», vient se poser la question de la suppression des végétaux nuisibles au bon développement des cultures, communément appelés « mauvaise herbes ».  

L’utilisation de pesticides étant, par voie de faits, complétement à l’encontre de l’agriculture biologique et de ses démarches environnementales, il est bien sûr impossible d’en utiliser pour lutter contre les nuisibles.


Désherber entre les rangs ne pose pas un problème majeur à l’agriculteur, dans la majorité des cas c’est un tracteur tirant des socs de binage ou des herses étrilles qui vient désherber entre les rangs. La difficulté principale est le désherbage dans le rang. La problématique se pose aussi pour une agriculture « classique ».C’est à la main ou à la binette que les ouvriers agricoles viennent désherber entre les plans de culture. Cette pratique est cependant souvent très coûteuse en termes de temps et d’argent pour les agriculteurs.

Se pose donc la problématique suivante : “\textit{Comment désherber efficacement entre les plans en agriculture biologique ?} “

L’objectif est donc d’offrir une solution mécanique moderne aux agriculteurs pour qu’ils puissent continuer de désherber leurs champs tout en respectant les normes de l’agriculture biologique. De plus, la digitalisation du monde agricole ouvre un nouveau champ de perspectives. En interconnectant les composants de la chaine de travail (robots, drones et humains), ainsi qu’en virtualisant les actions effectuées, nous offrons à l’opérateur humain une solution plus sécurisée, fiable et modulaire pour lui permettre un suivi et un contrôle optimal. A la précédente problématique, se rajoute donc une composante informatique visant à faciliter le suivi et le contrôle du désherbage entre les plans, pour un opérateur humain.

Le défi principal de la digitalisation dans le domaine agricole repose sur le fait que c'est un environnement dynamique, en changement constant. Les entités déployées (robots mobiles) et fixes (stations) doivent faire face en permanence aux aléas environnementaux (climats, changements de terrain, inconsistence dans la connexion dues à des facteurs extérieurs).
De plus, il est demandé aux robots de recueillir de l'information à l'aide de capteurs, dans cet environnement changeant. Il apparait donc comme une nécessité d'avoir des robots ayant l'impact le plus faible possible avec son environnement, tout en collectant suffisamment de données.

## Objectifs <a id="Objectifs"></a>

Le projet a pour objectif de proposer une architecture matérielle et logicielle à destination d'un ensemble de robots.
Le projet se divise en plusieurs étapes:

V0 - Analyse de l'environnement, étude des technologies et architecture à mettre en place

V1 - Réalisation d'un simulateur en python avec communication simultanée entre un serveur et plusieurs robots

V2 - Intégration de l'architecture soft et des API des différents capteurs

V3 - Migration sous ROS

V4 - Déploiement en grandeur nature

## Architecture générale <a id="Archi G"></a>

![Architecture](docs\img\CoeurArchi.jpg)

Le Framework est décomposé sous forme de noeuds indépendants.
On distingue 2 entités physiques différentes:
- Les robots, contenant les modules IA_Robot, Navigation et Sensors
- Le serveur, contenant les modules IA_Serveur et Local Server.

Ce coeur d'architecture présente la possibilité d'ajouter facilement des modules indépendants, ce qui est important notamment pour le rajout de capteurs par la suite.

Lors d'une action du robot, il faut prendre en compte le guidage automatique du véhicule, ainsi que la mise en oeuvre automatique des actions. Pour cela, différents modules sont activés.

![Infrastructure logicielle pour la mise en oeuvre automatique des actions](docs\img\AIF.jpg)


![Infrastructure logicielle pour la mise en oeuvre automatique des actions](docs\img\AVG.jpg)


## Architecture matérielle <a id="Archi M"></a>

![](docs\img\Archi_Generale_Lora.jpg)

## Architecture Logicielle <a id="Archi L"></a>

## Outputs <a id="Outputs"></a>

### IHM
![IHM](docs\img\front.PNG)

## Lancement <a id="Lancement"></a>

Le fichier Python launchRobot.py permet de lancer l'initialisation du robot. C'est un fichier test pour vérifier que l'initialisation des composants est correcte, et que l'on peut ensuite charger des infos, envoyer et recevoir des messages. Au niveau fonctionnement, on charge un XML contenant des informations relatives au type de robot. Les composants relatifs à l'archi robot sont ensuite initialisés. On ouvre ensuite un serveur socket pour écouter les communications entrantes.


Le fichier Python launchServeur.py va télécharger des informations relatives à l'environnement, puis mettre en place l'architecture pour communiquer avec les robots.

Lancer d'abord les robots indépendamment, puis le serveur, et attendez la connexion. Un message de mapping va ensuite être échangé, du serveur vers le robot (test).
