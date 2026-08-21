Project description
======================

OC Lettings is a web application built with the Django framework, designed for a
vacation rental agency. It lets visitors browse the available rentals and the
associated user profiles, and provides an admin interface to manage this data on a
day-to-day basis.

The application is organized into several independent modules, each responsible for
a specific area of the site.

oc_lettings_site application
------------------------------

This application forms the backbone of the project. It gathers the site's general
configuration (Django settings, main routing), the home page, and the custom error
pages (404 and 500), ensuring a consistent experience even when something goes
wrong.

lettings application
----------------------

The Lettings application handles everything related to the properties available for
rent. It allows browsing the list of available rentals as well as the detail of each
one, including its title and address.

profiles application
----------------------

The Profiles application manages the site's user profiles. It allows browsing the
list of registered profiles as well as the information specific to each user, such
as their favorite city.

Infrastructure
----------------

The site is containerized with Docker, ensuring an identical runtime environment
between local development and production. Its deployment is automated through a
continuous integration and delivery pipeline, and its health in production is
monitored using Sentry.
