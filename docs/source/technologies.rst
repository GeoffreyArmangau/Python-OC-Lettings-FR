Technologies and programming languages
============================================

The project relies on several technologies and programming languages.

- Python and the Django framework for building the web application (ORM, routing,
  templates, etc.).
- SQLite for the database, which is simple to set up and well suited to the
  project's needs.
- HTML, CSS with the Bootstrap framework and JavaScript for building the web pages
  and client-side interactivity (frontend).
- Docker for containerizing the application, ensuring a consistent runtime
  environment between development and production.
- pytest for unit and integration tests, ensuring code quality and application
  reliability.
- Sentry for error monitoring and centralized application logging in production.
- Gunicorn as the WSGI server running the application in production.
- Whitenoise for serving static files directly from the Django application in
  production.
- python-dotenv for loading environment variables from a local ``.env`` file.
