# PyQt5 Login

This project demonstrates how to create a simple user login system using PyQt5, where user credentials are fetched from a db.json file. The application allows users to enter their credentials (username and password), validates them against the data stored in the JSON file, and provides feedback on the login status.


## Features
- **User Login:** Users can log in by entering a username and password.
- **JSON File Storage:** User data is stored in a db.json file.
- **PyQt5 Interface:** The user interface is created using PyQt5.
- **Login Validation:** The system validates the username and password against the data in the db.json file.
- **Error Handling:** If incorrect credentials are provided, an error message will be displayed.

## Prerequisites
Before running the project, make sure you have the following installed:

- Python 3.x
- PyQt5 library

You can install the necessary dependencies using pip:

```bash
pip install PyQt5
```
## File Structure
```bash
PyQt5-Login-System
├── db.json            # The JSON file containing user data
├── main.py            # The main Python script for running the application
├── README.md          # This README file
```

## How It Works
**1. User Interface (PyQt5)**
The application utilizes PyQt5 to create a simple graphical user interface (GUI). It contains two input fields for entering the username and password and a login button to trigger the authentication process.

**2. Loading User Data**
The db.json file is loaded in the Python code to retrieve the user credentials. The user information is stored as a list of dictionaries inside the JSON file.

**3. Login Validation**
Once the user enters their credentials and clicks the login button, the entered username and password are compared to the data in the db.json file. If a match is found, the user is successfully logged in. If not, an error message is displayed.

**4. Error Handling**
If an invalid username or password is entered, the system will show an error message to inform the user that the credentials are incorrect.

## Tech Stack
- PyQt5
- JSON
