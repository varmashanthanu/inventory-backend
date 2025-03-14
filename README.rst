===================
Aircraft Inventory & Maintenance Management System
===================

Setup Instructions
==================

1. Clone the Repo
------------------

.. code-block:: bash

    git clone https://github.com/varmashanthanu/inventory-backend.git

2. Create `.env` file from `.env-sample` file and update as needed
------------------------------------------------------------------

.. code-block:: bash

    cp .env-sample .env

3. Run manage migrate
---------------------

.. code-block:: bash

    python manage.py migrate

4. Run collectstatic
--------------------

.. code-block:: bash

    python manage.py collectstatic

5. Run createsuperuser and follow the instructions
--------------------------------------------------

.. code-block:: bash

    python manage.py createsuperuser

6. Run the server with runserver
-------------------------------

.. code-block:: bash

    python manage.py runserver

7. Navigate to /api/docs to get the API documentation
-----------------------------------------------------

Open your web browser and go to:

    http://127.0.0.1:8000/api/docs