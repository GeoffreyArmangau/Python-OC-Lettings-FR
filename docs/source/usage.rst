Usage guide
=============

This page walks through the site's main use cases. It assumes the site is already
running locally — see :doc:`quickstart` if it is not.

Browse the available lettings
--------------------------------

1. Open ``http://localhost:8000/lettings/``.
2. The page lists every available rental, by title.
3. Click a listing's title to open its detail page, showing the title and the full
   address (number, street, city, state, zip code, country).

Browse the user profiles
--------------------------------

1. Open ``http://localhost:8000/profiles/``.
2. The page lists every registered profile, by username.
3. Click a username to open its detail page, showing the username and the user's
   favorite city (if set).

Manage the data as an administrator
--------------------------------------

1. Open ``http://localhost:8000/admin/``.
2. Log in with an administrator account. In a fresh local install with the demo
   database, use ``admin`` / ``Abc1234!``.
3. From the admin index, you can create, edit and delete:

   - **Lettings** and **Addresses** (lettings app).
   - **Profiles** (profiles app).
   - Django's own users and groups.

4. Changes made in the admin are reflected immediately on the public
   ``/lettings/`` and ``/profiles/`` pages.

Handling of missing records
--------------------------------

Visiting a letting or profile detail page with an id/username that does not exist
(e.g. ``/lettings/9999/``) raises a ``DoesNotExist`` error, which Django surfaces
as a 500 error page (see :doc:`api`). This is expected behavior: these pages are
only meant to be reached by following valid links from the listing pages.
