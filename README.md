# billing
This is a Django REST framework-based application for managing investors, investments, bills, and cash calls. The application allows creating and managing records for investors and their investments, generating bills based on specific strategies, and grouping them into cash calls for further processing.

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
    git clone https://github.com/yourusername/invoicing.git
    cd invoicing
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Apply migrations**:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running the Project

1. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

2. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:8000/`.

## App Structure

- `billing/`: Contains the main application code.
  - `admin.py`: Admin configurations.
  - `models.py`: Database models.
  - `serializers.py`: Serializers for API.
  - `views.py`: API views.
  - `urls.py`: URL configurations.
  - `bill_strategies.py`: Strategies for generating bills.
  - `tests/`: Directory for tests.
    - `test_models.py`: Tests for models.
    - `test_views.py`: Tests for views.
    - `test_serializers.py`: Tests for serializers.
  - `management/commands/`: Custom management commands.
    - `generate_data.py`: Command to generate investors and their investments.
    - `generate_bills.py`: Command to generate bills.
    - `generate_cash_calls.py`: Command to generate cash calls.

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
  - `GET /bills/group_by_investor/`: List bills grouped by investor.

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

    This command creates 10 investors and between 0 to 1 investment per investor per year since 2017 (ie. a maximum of 8 investments for 1 investor).

- **Generate Bills**:

    ```sh
    python manage.py generate_bills
    ```

    This command generates bills for the CURRENT YEAR investments based on the predefined strategies(bill_strategies.py).

  - **Generate Cash Calls**:

    ```sh
    python manage.py generate_cash_calls
    ```

    This command generates a maximum of 1 cash call per investor for the CURRENT YEAR bills (status of the cash call created = "created").
    Note: If a cash call has already been created during the current year for a given investor and its status = "paid", all the bills included in this cash call wont be included in the new cash call created.


## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Additional Information

- The project uses Django REST framework for building the API.
- Timestamps (`created_at` and `updated_at`) are automatically managed by Django.
- The `generate_bills.py` command ensures no duplicate bills are created within the same year.
- The `CashCall` model tracks the status of cash calls with statuses: `created`, `validated`, `sent`, `paid`, and `overdue`.

Thanks for the reading!
