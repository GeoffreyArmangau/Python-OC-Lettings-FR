Installation
============

This page details the complete local installation of the project, for a development
environment.

Prerequisites
-------------

- A GitHub account with read access to the repository.
- Git.
- Python, version 3.6 or higher.
- SQLite3 (usually already installed with Python).

Clone the repository
---------------------

.. code-block:: bash

   git clone https://github.com/GeoffreyArmangau/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Create the virtual environment
-------------------------------

A virtual environment isolates the project's dependencies from the rest of the
system.

.. code-block:: bash

   python -m venv venv

Then activate it:

- macOS / Linux: ``source venv/bin/activate``
- Windows (PowerShell): ``.\venv\Scripts\Activate.ps1``

Install dependencies
----------------------------

.. code-block:: bash

   pip install -r requirements.txt

Configure environment variables
-------------------------------------------

The project uses a ``.env`` file (not versioned) for its sensitive settings. Copy the
provided template, then fill it in:

.. code-block:: bash

   cp .env.example .env

The expected variables are documented in ``.env.example``: a Django secret key
specific to your environment, and optionally a Sentry DSN if you want to test error
monitoring locally.

To generate a Django secret key:

.. code-block:: bash

   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Run the site
----------------

.. code-block:: bash

   python manage.py runserver

The site is then available at ``http://localhost:8000``. The provided SQLite
database already contains demo data (several rentals and profiles), so no
migration is needed for a first install.
