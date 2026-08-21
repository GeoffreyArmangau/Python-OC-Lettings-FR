Application interfaces
=========================

OC Lettings does not expose a REST/JSON API. Its programming interface is a set of
server-rendered HTML routes, handled by Django views. This page documents each
route: its URL, its view function, and the data it renders.

Site routes
----------------

.. list-table::
   :header-rows: 1

   * - Route
     - View
     - Description
   * - ``/``
     - ``oc_lettings_site.views.index``
     - Home page.
   * - ``/admin/``
     - Django admin
     - Admin interface (see :doc:`database`).

lettings routes
------------------

Mounted under ``/lettings/``, namespace ``lettings``.

.. list-table::
   :header-rows: 1

   * - Route
     - View
     - Description
   * - ``/lettings/``
     - ``lettings.views.index``
     - Lists all lettings.
   * - ``/lettings/<int:letting_id>/``
     - ``lettings.views.letting``
     - Detail page for one letting (title and address). Raises
       ``Letting.DoesNotExist`` — surfaced as a 500 error page — if
       ``letting_id`` is unknown.

profiles routes
------------------

Mounted under ``/profiles/``, namespace ``profiles``.

.. list-table::
   :header-rows: 1

   * - Route
     - View
     - Description
   * - ``/profiles/``
     - ``profiles.views.index``
     - Lists all profiles.
   * - ``/profiles/<str:username>/``
     - ``profiles.views.profile``
     - Detail page for one profile (associated user's username and favorite
       city). Raises ``Profile.DoesNotExist`` — surfaced as a 500 error page —
       if the username is unknown.

Error pages
----------------

When ``DEBUG`` is disabled (production), unhandled 404 and 500 conditions render
the custom ``404.html`` and ``500.html`` templates instead of Django's default
debug pages.
