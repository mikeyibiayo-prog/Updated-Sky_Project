Sky Project

A full stack Django web application developed as part of a university software development group project for Sky Engineering teams. The system replaces a manually maintained Excel spreadsheet with a centralised web platform for managing engineering teams, departments, dependencies, repositories, communication channels, and internal collaboration tools.

The project was built using Django, Python, SQLite, Bootstrap, HTML, CSS, and JavaScript.

Project Overview

The goal of the application is to provide a secure and scalable internal portal where users can:

- Search engineering teams and departments
- View organisational structures and dependencies
- Manage messages and communication
- Schedule meetings
- Generate reports
- Access team repositories and contact channels
- Maintain up-to-date engineering team information

The system was designed following Agile development practices and includes both frontend and backend functionality.

Features

Authentication System
- User registration
- Secure login/logout
- Password management
- User profile handling
- Django admin access

Team Management
- View all engineering teams
- Search teams and departments
- Display dependencies
- View team responsibilities and descriptions
- Team contact information

Messaging System
- Inbox
- Sent messages
- Draft messages
- Create new messages
- Internal communication workflow

Scheduling System
- Schedule meetings
- Weekly and monthly schedules
- Upcoming meetings dashboard
- Meeting platform and message support

Reports and Visualisation
- Generate reports
- Summary statistics
- Team management reporting
- Data visualisation support

Database and Backend
- SQLite database integration
- Django ORM models
- CRUD functionality
- Admin dashboard
- Relational database structure

Technologies Used

Backend
- Python
- Django
- SQLite

Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

Development Tools
- Git & GitHub
- VS Code
- DB Browser for SQLite
- Draw.io
- Figma

Software Engineering Concepts Applied

This project involved practical experience in:
- Full stack web development
- Database modelling and ERD design
- Agile software development
- Software testing
- UI/UX design
- Authentication and security
- CRUD operations
- Team collaboration and version control

Project Structure

Updated-Sky_Project/
│
├── accounts/
├── messages/
├── templates/
├── static/
├── Sky_project/
├── db.sqlite3
├── manage.py
└── requirements.txt

Installation

Clone the repository

git clone https://github.com/mikeyibiayo-prog/Updated-Sky_Project.git

cd Updated-Sky_Project

Create virtual environment

python -m venv venv

Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Create superuser

python manage.py createsuperuser

Run development server

python manage.py runserver

Example Functionalities

User Features
- Register and log into the system
- Search engineering teams
- Send and receive internal messages
- View organisational structures
- Schedule meetings

Admin Features
- Manage users and permissions
- Add/edit/delete teams
- Manage departments
- Generate reports
- Access database records through Django Admin

Learning Outcomes

Through this project I improved my skills in:
- Django backend development
- SQL and relational databases
- REST-style application structure
- Frontend UI design
- Git version control
- Team-based software engineering
- Software testing and debugging
- Problem solving and project management

Future Improvements

Potential future improvements include:
- Real-time messaging
- REST API integration
- Advanced analytics dashboards
- Role-based access control
- Docker deployment
- PostgreSQL migration
- Cloud deployment
- Improved dependency visualisation

Author

Michael Ibiayo
