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
