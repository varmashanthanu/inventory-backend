===================
Aircraft Inventory & Maintenance Management System
===================

Setup Instructions
==================

1. Clone the Repo
------------------

.. code-block:: bash

    git clone https://github.com/varmashanthanu/inventory-backend.git

2. Create and activate a virtual environment
--------------------------------------------

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate

3. Create `.env` file from `.env-sample` file and update as needed
------------------------------------------------------------------

.. code-block:: bash

    cp .env-sample .env

4. Generate a secret key and update the `.env` file
---------------------------------------------------

.. code-block:: python

    import secrets

    def generate_secret_key():
        return secrets.token_urlsafe(50)

    print(generate_secret_key())

Copy the generated secret key and update the `SECRET_KEY` field in the `.env` file.

5. Run manage migrate
---------------------

.. code-block:: bash

    python manage.py migrate

6. Run collectstatic
--------------------

.. code-block:: bash

    python manage.py collectstatic

7. Run createsuperuser and follow the instructions
--------------------------------------------------

.. code-block:: bash

    python manage.py createsuperuser

8. Run the server with runserver
-------------------------------

.. code-block:: bash

    python manage.py runserver

9. Navigate to /api/docs to get the API documentation
-----------------------------------------------------

Open your web browser and go to:

    http://127.0.0.1:8000/api/docs