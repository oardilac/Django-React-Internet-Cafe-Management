# Internet Cafe Management Web Application

This project is a web-based application developed using Django REST framework to facilitate the management of an internet cafe business. The application provides several features such as managing computer sessions, tracking payments, handling reservations, and user authentication.

## Features

- Secure user registration and login using JWT authentication for secure API endpoints.
- Admin interface for managing computer sessions, payments, reservations and user profiles
- Manage computer sessions with functionality to create, update, delete, and view sessions
- Handle payments related to sessions
- Handle reservations with tariff rates
- Auto generation of Swagger and Redoc documentation

## Requirements

Before starting make sure you have the following installed:

- Python (3.9)
- Docker (for containerization)
- Docker Compose (for multi-container Docker applications)

## Installation

1. Clone this repository: `git clone https://github.com/oardilac/Django-React-Internet-Cafe-Management.git`
2. Go to the project directory: `cd Django-React-Internet-Cafe-Management`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Run the server: `python manage.py runserver`

## Built With

- Django: The web framework used for building the application
- Django REST Framework: A powerful and flexible toolkit for building Web APIs
- PostgreSQL: Our main database
- Docker: For containerization and easy deployment
- drf-yasg: To auto generate real Swagger/OpenAPI 2.0 specifications with Django Rest Framework
- Simple JWT: A JSON Web Token authentication plugin for the Django REST Framework

## Usage

Open your favorite API client (like Postman) to send requests to the API endpoints.

## Documentation

You can view the auto-generated OpenAPI documentation at `/swagger/` and `/redoc/` endpoints.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- Oliver Ardila
- Sebastian Escobar
- Haxell Gomez

## License

BSD License

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration