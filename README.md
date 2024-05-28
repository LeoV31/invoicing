# invoicing
This is a Django REST framework-based application for managing investors, investments, bills, and cash calls. The application allows creating and managing records for investors and their investments, generating bills based on specific strategies, and grouping them into cash calls for further processing.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Custom Commands](#custom-commands)
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

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Load initial data (optional)**:

    ```sh
    python manage.py loaddata initial_data.json
    ```

## Running the Project

1. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

2. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Running Tests

To run the tests, use the following command:






