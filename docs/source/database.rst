Database structure and data models
====================================

The project uses two custom apps, each owning its own models, plus Django's
built-in ``auth.User`` model for authentication.

lettings app
----------------

Address
~~~~~~~~~

A postal address, owned by exactly one Letting.

.. list-table::
   :header-rows: 1

   * - Field
     - Description
   * - ``number``
     - House/building number (positive integer, max 4 digits).
   * - ``street``
     - Street name (up to 64 characters).
   * - ``city``
     - City name (up to 64 characters).
   * - ``state``
     - 2-letter state code (e.g. a US state abbreviation).
   * - ``zip_code``
     - Postal code (positive integer, max 5 digits).
   * - ``country_iso_code``
     - 3-letter ISO country code.

Letting
~~~~~~~~~

A rental listing, paired with a single Address.

.. list-table::
   :header-rows: 1

   * - Field
     - Description
   * - ``title``
     - Display name of the listing (up to 256 characters).
   * - ``address``
     - One-to-one link to its Address.

profiles app
----------------

Profile
~~~~~~~~~

Extra profile data attached one-to-one to a Django ``auth.User``.

.. list-table::
   :header-rows: 1

   * - Field
     - Description
   * - ``user``
     - One-to-one link to the associated ``auth.User``.
   * - ``favorite_city``
     - Optional free-text favorite city (up to 64 characters).

Relationships
----------------

- One ``Address`` belongs to exactly one ``Letting`` (one-to-one).
- One ``auth.User`` has exactly one ``Profile`` (one-to-one).
- ``Letting`` and ``Profile`` are otherwise independent of each other.

Admin interface
------------------

``Address``, ``Letting`` and ``Profile`` are all registered with the Django admin
site, so staff users can create, edit and delete records at ``/admin/`` without
writing any code.
