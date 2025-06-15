# CRM Project

This is a simple CRM (Customer Relationship Management) web application built with Django, made with Nothing OS style.
## login 
![image](https://github.com/user-attachments/assets/cf2c45dd-1ca5-4656-9535-aa4ceb080eba)

## Home
![image](https://github.com/user-attachments/assets/196598a8-56d8-4f5e-8ed3-f07795960e9e)

## CRUD Operations 
![image](https://github.com/user-attachments/assets/2db73c38-45fd-4d41-a30e-eddca0813f5b)
![image](https://github.com/user-attachments/assets/e7b7cc1b-99e5-44e8-b3ab-ca93d1a9085e)
![image](https://github.com/user-attachments/assets/162914ea-f9bf-4d97-b714-06971a35a123)

## Features
- Add, update, and view customer records
- Simple web UI with templates for home, add, update, and view records
- Uses SQLite as the database backend

## Project Structure
```
CRM/
├── CRM/                # Main Django project directory
│   ├── web/            # Django app for CRM logic
│   ├── templates/      # HTML templates
│   ├── db.sqlite3      # SQLite database file
│   └── manage.py       # Django management script
├── README.md           # Project documentation (this file)
```

## Getting Started

### Prerequisites
- Python 3.x
- pip
- Django (install with `pip install django`)

### Running the Project
1. Navigate to the project directory:
   ```bash
   cd CRM
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Notes
- Default database is SQLite, stored as `db.sqlite3` in the project folder.
- Templates are located in `CRM/templates/`.
- Main app logic is in `CRM/web/`.

## License
This project is for educational/demo purposes.
#
