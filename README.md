# Invoicing Project / Billing App

This is a Django REST framework-based application for managing investors, investments, bills, and cash calls of a French VC-fund. The application allows creating and managing records for investors and their investments, generating bills based on specific strategies, and grouping them into cash calls for further processing.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [App Structure](#app-structure)
- [API Endpoints](#api-endpoints)
- [Custom Commands](#custom-commands)
- [Running Tests](#running-tests)
- [Additional Information](#additional-information)

## Requirements

- Python 3.11
- Django 5.0.6
- Django REST framework
- pytest (for testing)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/LeoV31/invoicing.git
    cd invoicing
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Fill the database with relevant data**:

    You can fill your database with random investors and investments by running :
   
   ```sh
    python manage.py generate_data
    ```
   
   Then you can automatically create the corresponding bills and cash calls for the current year with :
   
   ```sh
    python manage.py generate_bills
    python manage.py generate_cash_calls
    ```

## Running the Project

1. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

2. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:8000/`.

    You can now navigate through the different records (investors, investments, bills, and cash calls)!

## Project Structure

- `billing/`: Contains the main application code.
  - `__init__.py`: Marks the directory as a Python package.
  - `admin.py`: Admin configurations.
  - `apps.py`: Application configuration
  - `models.py`: Database models.
  - `serializers.py`: Serializers for API.
  - `views.py`: API views.
  - `urls.py`: URL configurations.
  - `bill_strategies.py`: Strategies for generating bills.
  - `migrations/`: Contains migration files for database schema changes.
  - `tests/`: Directory for tests.
    - `test_models.py`: Tests for models.
    - `test_views.py`: Tests for views.
    - `test_serializers.py`: Tests for serializers.
  - `management/commands/`: Custom management commands.
    - `generate_data.py`: Command to generate investors and their investments.
    - `generate_bills.py`: Command to generate bills.
    - `generate_cash_calls.py`: Command to generate cash calls.
- `invoicing/`: Contains project-wide settings and configurations.
    - `__init__.py`: Marks the directory as a Python package.
    - `asgi.py`: ASGI configuration.
    - `settings.py`: Project settings.
    - `urls.py`: URL routing for the project.
    - `wsgi.py`: WSGI configuration.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: The project's readme file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `pytest.ini`: Configuration file for pytest.
- `requirements.txt`: A file listing the project's dependencies.

## API Endpoints

The application exposes several API endpoints:

- **Investors**:
  - `GET /investors/`: List all investors.
  - `POST /investors/`: Create a new investor.
  - `GET /investors/{id}/`: Retrieve details of a specific investor.
  - `PUT /investors/{id}/`: Update details of a specific investor.
  - `DELETE /investors/{id}/`: Delete a specific investor.

- **Investments**:
  - `GET /investments/`: List all investments.
  - `POST /investments/`: Create a new investment.
  - `GET /investments/{id}/`: Retrieve details of a specific investment.
  - `PUT /investments/{id}/`: Update details of a specific investment.
  - `DELETE /investments/{id}/`: Delete a specific investment.

- **Bills**:
  - `GET /bills/`: List all bills.
  - `POST /bills/`: Create a new bill.
  - `GET /bills/{id}/`: Retrieve details of a specific bill.
  - `PUT /bills/{id}/`: Update details of a specific bill.
  - `DELETE /bills/{id}/`: Delete a specific bill.

- **Grouped Bills**:
  - `GET /grouped-bills/`: List all bills grouped by investor.

- **Cash Calls**:
  - `GET /cashcalls/`: List all cash calls.
  - `POST /cashcalls/`: Create a new cash call.
  - `GET /cashcalls/{id}/`: Retrieve details of a specific cash call.
  - `PUT /cashcalls/{id}/`: Update details of a specific cash call.
  - `DELETE /cashcalls/{id}/`: Delete a specific cash call.

## Custom Commands

The application includes custom Django management commands:

- **Generate Investors and Investments**:

    ```sh
    python manage.py generate_data
    ```

    This command creates 10 investors. Each investor will have between 0 to 1 investment per year since 2017, resulting in a maximum of 8 investments per investor.

- **Generate Bills**:

    ```sh
    python manage.py generate_bills
    ```

    This command generates bills for the current year based on the predefined strategies (see bill_strategies.py).

- **Generate Cash Calls**:

    ```sh
    python manage.py generate_cash_calls
    ```

    This command generates at most one cash call per investor for the current year's bills. The status of the newly created cash call will be by default "created".
    Note: If a cash call with the status "paid" already exists for an investor in the current year, the bills included in that paid cash call will not be included in the new cash call.

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Additional Information

- **Timestamps**:
  - `created_at` and `updated_at` fields are automatically managed by Django. They are used to track when a record is created and last updated, respectively.
  - `date_added` is a specific field used in the `Investment` model to indicate the date when the investment was made.

- **Admin Interface**: The project includes an admin interface for managing the models. You can access the Django admin interface at `http://127.0.0.1:8000/admin/`. Ensure you have created a superuser to log in and manage the records.

  To create a superuser, run:
  
  ```sh
  python manage.py createsuperuser
  ```

- **Bill Generation Strategies**: The project uses different strategies to generate bills (MembershipBillStrategy, UpfrontBillStrategy, YearlyBillStrategy). Each strategy calculates fees based on predefined rules and conditions.
