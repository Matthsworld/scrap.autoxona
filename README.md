# Scrap.Autoxona

Scrap.Autoxona is a Flask web application that allows users to list their vehicles for scrap, book appointments for vehicle assessment, and request free instant online car valuations. The application includes features for user authentication, form submissions, and admin functionalities for managing listings and appointments.

## Features

- User authentication (Signup, Login, Logout)
- List a scrap vehicle
- Book an appointment for vehicle assessment
- Request a free instant online car valuation
- Admin functionalities:
  - View all appointments
  - Delete appointments and listings
  - Mark appointments as attended or not attended
  - Respond to quote requests

## Installation

### Prerequisites

- Python 3.7+
- Virtual environment (recommended)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/matthsworld/scrap.autoxona.git
   cd scrap.autoxona

Create and activate a virtual environment:

### bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install the required packages:

### bash

pip install -r requirements.txt
Configure environment variables (optional):

Create a .env file in the project root and add the following variables:
env

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db

## Initialize the database:

### bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## Run the application:

### bash
flask run

Access the application at http://127.0.0.1:5000/.

## Project Structure

scrap.autoxona/
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── list_scrap.html
│   │   ├── book_appointment.html
│   │   ├── view_quotes.html
│   │   ├── respond_quote.html
│   │   ├── appointments.html
│   └── static/
│       └── images/
│           └── your_image.jpg
├── migrations/
├── config.py
├── requirements.txt
├── .env
└── README.md

# Usage
## User Features

Home Page
View a sliding image with a caption and a button to list a scrap vehicle.
Request a free instant online car valuation by filling out a form.
List a Scrap
Authenticated users can list their vehicle for scrap by providing necessary details.
Book Appointment
Authenticated users can book an appointment for vehicle assessment by submitting a form with required details and photos.

## Admin Features
View and Manage Appointments
Admins can view all appointments, delete them, and mark them as attended or not attended.
View and Respond to Quote Requests
Admins can view all quote requests and respond to them.

## Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bugfix.
Make your changes and commit them with a descriptive message.
Push your changes to your forked repository.
Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

Flask
SQLAlchemy
Flask-WTF
Flask-Migrate
Werkzeug

## Contact

For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer at `matthsworld@gmail.com`