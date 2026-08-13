## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Surveillance des erreurs (Sentry)

Le site utilise [Sentry](https://sentry.io) pour la surveillance des erreurs et la
centralisation des logs applicatifs. Aucun identifiant Sentry n'est stocké dans le code
source : tout passe par des variables d'environnement chargées depuis un fichier `.env`
local (non versionné).

##### Configurer Sentry pour la première fois

1. Créer un compte sur [sentry.io](https://sentry.io) (ou utiliser un compte existant).
2. Créer un nouveau projet, plateforme **Django**. Sur l'écran de création, activer au
   minimum les fonctionnalités **Error monitoring** et **Logging** (les autres — Tracing,
   Profiling, Application Metrics — ne sont pas utilisées par ce projet).
3. Une fois le projet créé, Sentry affiche un DSN (une URL du type
   `https://xxxx@xxxx.ingest.xx.sentry.io/xxxx`) : le copier.
4. À la racine du projet (`Python-OC-Lettings-FR/`), copier `.env.example` vers `.env` :
   - macOS/Linux : `cp .env.example .env`
   - Windows (PowerShell) : `Copy-Item .env.example .env`
5. Renseigner les variables dans `.env` :
   - `SENTRY_DSN` : le DSN copié à l'étape 3.
   - `DJANGO_SECRET_KEY` : une clé secrète Django propre à votre environnement (ne
     jamais réutiliser une clé qui a déjà été commitée). Pour en générer une :
     `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
6. Relancer le serveur (`python manage.py runserver`) : Sentry s'initialise
   automatiquement au démarrage si `SENTRY_DSN` est renseigné.

##### Vérifier que ça fonctionne

- Visiter une URL de détail avec un identifiant inexistant, par exemple
  `http://localhost:8000/lettings/99999/` ou `http://localhost:8000/profiles/personne-nexiste-pas/` :
  la page 500 personnalisée doit s'afficher.
- Dans le terminal qui exécute `runserver`, une ligne de log de niveau `ERROR` doit
  apparaître (ex. `ERROR lettings.views Letting with id=99999 does not exist`).
- Dans le tableau de bord Sentry (menu **Issues**), l'erreur correspondante
  (`Letting.DoesNotExist` ou `Profile.DoesNotExist`) doit apparaître après quelques
  secondes.

##### Notes pour aller plus loin

- Sentry est volontairement désactivé pendant l'exécution de la suite de tests
  (`pytest`), pour ne pas polluer le tableau de bord avec les erreurs déclenchées
  intentionnellement par les tests (voir `RUNNING_TESTS` dans
  `oc_lettings_site/settings.py`).
- Les niveaux de logs (quels messages sont gardés en contexte, lesquels déclenchent un
  vrai incident Sentry) sont configurables via `LOGGING` et `LoggingIntegration` dans
  `oc_lettings_site/settings.py`.
- Pour ajouter des logs dans une nouvelle vue ou fonction, utiliser
  `logger = logging.getLogger(__name__)` en haut du fichier, puis `logger.info(...)` /
  `logger.error(...)` selon la gravité — voir `lettings/views.py` ou
  `profiles/views.py` pour des exemples.

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Récapitulatif

Le déploiement est entièrement automatisé par un pipeline GitHub Actions
(`.github/workflows/ci-cd.yml`), composé de 3 étapes :

1. **Build & test** : à chaque `push`, sur n'importe quelle branche, installe les
   dépendances, lance le linting (`flake8`) et la suite de tests avec vérification de la
   couverture (`pytest --cov-fail-under=80`).
2. **Conteneurisation** : uniquement sur la branche `master`, et seulement si l'étape
   précédente réussit, construit l'image Docker et la pousse sur Docker Hub, avec deux
   tags : `latest` et le hash du commit.
3. **Déploiement** : uniquement sur `master`, et seulement si la conteneurisation
   réussit, appelle le "Deploy Hook" de Render pour déclencher le déploiement de la
   nouvelle image.

Un push sur une autre branche que `master` ne déclenche donc que le linting et les
tests, jamais la conteneurisation ni le déploiement.

### Configuration requise

- Un dépôt sur [Docker Hub](https://hub.docker.com) pour héberger l'image (ce projet
  utilise `ageoff/python-oc-lettings-fr`).
- Un service web sur [Render](https://render.com), de type "Deploy an existing image
  from a registry", pointant vers ce dépôt Docker Hub.
- Sur ce service Render, les variables d'environnement suivantes :
  - `DJANGO_SECRET_KEY` : une clé secrète propre à l'environnement de production (ne
    jamais réutiliser une clé qui a déjà été commitée dans l'historique Git).
  - `DJANGO_DEBUG` : `False`.
  - `SENTRY_DSN` : optionnel mais recommandé, voir la section Sentry ci-dessus.
- Dans les paramètres GitHub du dépôt (**Settings > Secrets and variables >
  Actions**), 3 secrets :
  - `DOCKERHUB_USERNAME` : le nom d'utilisateur Docker Hub.
  - `DOCKERHUB_TOKEN` : un jeton d'accès Docker Hub dédié (droits Read & Write), pas le
    mot de passe du compte — à générer sur
    [hub.docker.com/settings/security](https://hub.docker.com/settings/security).
  - `RENDER_DEPLOY_HOOK_URL` : l'URL du "Deploy Hook" du service Render (visible dans
    **Settings > Deploy** du service).

### Étapes pour mettre en place le déploiement (à faire une seule fois)

1. Créer le dépôt sur Docker Hub.
2. Construire et pousser une première image manuellement — Render a besoin qu'une
   image existe déjà pour pouvoir créer un service qui pointe dessus :
   ```
   docker build -t <utilisateur>/<depot>:latest .
   docker push <utilisateur>/<depot>:latest
   ```
3. Créer le Web Service sur Render à partir de cette image, avec les variables
   d'environnement listées ci-dessus.
4. Récupérer l'URL du Deploy Hook du service Render.
5. Ajouter les 3 secrets GitHub listés ci-dessus.
6. Pousser sur `master` : le pipeline se charge de tous les déploiements suivants
   automatiquement, sans autre intervention manuelle.

### Vérifier qu'un déploiement s'est bien passé

- Ouvrir l'URL publique du service Render et vérifier que les pages se chargent
  normalement.
- Vérifier que les fichiers statiques (CSS, images) s'affichent correctement — c'est un
  site destiné aux consommateurs, l'apparence doit être identique à ce qui est vu en
  local.
- Vérifier que l'interface d'administration (`/admin/`) a le même rendu qu'en local (le
  CTO l'utilise fréquemment).

### Récupérer et lancer l'image en local avec Docker (une seule commande)

```
docker run -p 8000:8000 --env-file .env <utilisateur>/<depot>:latest
```

Cette commande télécharge l'image depuis Docker Hub si elle n'est pas déjà présente en
local, puis démarre le site — accessible sur `http://localhost:8000`. Le fichier `.env`
doit contenir au minimum `DJANGO_SECRET_KEY` (voir `.env.example`).
