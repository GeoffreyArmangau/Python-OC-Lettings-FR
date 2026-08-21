Quickstart
=================

This guide presents the minimal procedure to run the site locally. For a detailed
description of each step, see the :doc:`installation` page.

.. code-block:: bash

   git clone https://github.com/GeoffreyArmangau/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   python -m venv venv
   source venv/bin/activate          # or .\venv\Scripts\Activate.ps1 on Windows
   pip install -r requirements.txt
   cp .env.example .env
   python manage.py runserver

The site is then available at ``http://localhost:8000``.

A demo admin account is already present in the database: username ``admin``,
password ``Abc1234!``, accessible at ``http://localhost:8000/admin``.

Alternative with Docker
--------------------------

If Docker is installed, the site can also be run without setting up a local Python
environment:

.. code-block:: bash

   docker run -p 8000:8000 --env-file .env ageoff/python-oc-lettings-fr:latest

This command automatically downloads the image if needed, then starts the site —
see :doc:`deployment` for more details.
