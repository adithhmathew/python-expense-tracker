# Expense Tracker (Flask Web App)

## Description

A full-featured expense tracking web application built using Python and Flask.
The app allows users to manage daily expenses through a clean web interface with data storage and analysis features.

---

## Features

* Add expenses with amount, category, description, and date
* View all expenses in a structured layout
* Edit and delete existing expenses
* Search and filter expenses by category, description, or date
* Calculate total spending
* Category-wise summary
* Monthly expense tracking
* Clean and responsive UI using Bootstrap
* Persistent storage using CSV file

---

## Technologies Used

* Python
* Flask
* HTML
* Bootstrap (CSS framework)
* CSV (for data storage)

---

## Project Structure

expense_tracker/
│
├── app.py
├── requirements.txt
├── expenses.csv
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── add.html
│   ├── view.html
│   ├── edit.html
│   ├── summary.html
│   ├── total.html
│   └── monthly.html
├── README.md

---

## How to Run Locally

1. Clone the repository

2. Install dependencies:
   pip install -r requirements.txt

3. Run the application:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

---

## Deployment

This project is ready to be deployed using platforms like Render.

Start command used for deployment:
gunicorn app:app

---

## What I Learned

* Building full-stack web applications using Flask
* Handling user input through web forms
* Implementing CRUD operations (Create, Read, Update, Delete)
* File handling using CSV for persistent storage
* Data filtering and search functionality
* Using template inheritance in Flask (base.html)
* Designing responsive UI using Bootstrap
* Structuring and organizing a real-world project

---

## Future Improvements

* Replace CSV with a database (SQLite/MySQL)
* Add user authentication (login/signup)
* Add charts for data visualization
* Improve UI/UX further
* Deploy with persistent storage

---

## Acknowledgement

This project was built as part of my learning journey in Computer Science Engineering.
