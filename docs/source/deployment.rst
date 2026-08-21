Deployment
============

Overview
----------

Deployment is fully automated by a GitHub Actions pipeline
(``.github/workflows/ci-cd.yml``), made up of 3 stages:

1. **Build & test**: on every push, on any branch, installs dependencies, runs
   linting (``flake8``) and the test suite with a coverage check
   (``pytest --cov-fail-under=80``).
2. **Containerize**: only on the ``master`` branch, and only if the previous stage
   succeeds, builds the Docker image and pushes it to Docker Hub, with two tags:
   ``latest`` and the commit hash.
3. **Deploy**: only on ``master``, and only if containerization succeeds, calls
   Render's "Deploy Hook" to trigger the deployment of the new image.

A push to any branch other than ``master`` therefore only triggers linting and
tests — never containerization or deployment.

Required configuration
-------------------------

- A `Docker Hub <https://hub.docker.com>`_ repository to host the image (this
  project uses ``ageoff/python-oc-lettings-fr``).
- A `Render <https://render.com>`_ web service, of type "Deploy an existing image
  from a registry", pointing at that Docker Hub repository.
- On that Render service, the following environment variables:

  - ``DJANGO_SECRET_KEY``: a secret key specific to the production environment
    (never reuse a key that has already been committed to Git history).
  - ``DJANGO_DEBUG``: ``False``.
  - ``SENTRY_DSN``: optional but recommended, for error monitoring.

- In the repository's GitHub settings (**Settings > Secrets and variables >
  Actions**), 3 secrets:

  - ``DOCKERHUB_USERNAME``: the Docker Hub username.
  - ``DOCKERHUB_TOKEN``: a dedicated Docker Hub access token (Read & Write), not
    the account password — generate one at
    `hub.docker.com/settings/security <https://hub.docker.com/settings/security>`_.
  - ``RENDER_DEPLOY_HOOK_URL``: the URL of the Render service's "Deploy Hook"
    (visible under **Settings > Deploy** of the service).

One-time setup steps
------------------------

1. Create the repository on Docker Hub.
2. Build and push a first image manually — Render needs an image to already exist
   in order to create a service pointing at it:

   .. code-block:: bash

      docker build -t <username>/<repository>:latest .
      docker push <username>/<repository>:latest

3. Create the Web Service on Render from that image, with the environment
   variables listed above.
4. Retrieve the Render service's Deploy Hook URL.
5. Add the 3 GitHub secrets listed above.
6. Push to ``master``: the pipeline then handles every subsequent deployment
   automatically, with no further manual steps.

Verifying a deployment
-------------------------

- Open the Render service's public URL and check that pages load normally.
- Check that static files (CSS, images) render correctly — this is a
  consumer-facing site, so it must look identical to the local version.
- Check that the admin interface (``/admin/``) renders the same as locally.

Pulling and running the image locally with Docker
------------------------------------------------------

.. code-block:: bash

   docker run -p 8000:8000 --env-file .env <username>/<repository>:latest

This command downloads the image from Docker Hub if it is not already present
locally, then starts the site — available at ``http://localhost:8000``. The
``.env`` file must at minimum contain ``DJANGO_SECRET_KEY`` (see
``.env.example``).
