Description du projet
======================

OC Lettings est une application web développée avec le framework Django, destinée à
une agence de location de logements de vacances. Elle permet aux visiteurs de
consulter les locations disponibles ainsi que les profils des utilisateurs associés,
et met à disposition une interface d'administration pour gérer ces données au
quotidien.

L'application est organisée en plusieurs modules indépendants, chacun responsable
d'un domaine précis du site.

Application oc_lettings_site
------------------------------

Cette application constitue le socle du projet. Elle regroupe la configuration
générale du site (paramètres Django, routage principal), la page d'accueil, ainsi que
les pages d'erreur personnalisées (404 et 500), afin de garantir une expérience
cohérente même en cas de problème.

Application lettings
----------------------

L'application Lettings est responsable de tout ce qui concerne les logements proposés
à la location. Elle permet de consulter la liste des locations disponibles ainsi que
le détail de chacune d'entre elles, notamment son titre et son adresse.

Application profiles
----------------------

L'application Profiles gère les profils des utilisateurs du site. Elle permet de
consulter la liste des profils enregistrés ainsi que les informations propres à
chaque utilisateur, telles que sa ville favorite.

Infrastructure
----------------

Le site est conteneurisé avec Docker, ce qui garantit un environnement d'exécution
identique entre le développement local et la production. Son déploiement est
automatisé par un pipeline d'intégration et de livraison continues, et son bon
fonctionnement est surveillé en production grâce à l'outil Sentry.
