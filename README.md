# Hospital Management System

A comprehensive Hospital Management System to manage patient records, doctor schedules, appointments, surgeries, billing, drugs, tests, and much more. Built using Python and MySQL for efficient database management.

---

## Features

- **Patient Management**
  - View, add, search, admit, discharge, and migrate patients.
  
- **Doctor Management**
  - Manage doctor records, update working hours, and handle appointments.

- **Appointment Management**
  - Schedule, view, and update appointments for doctors and patients.
  - Support for conflict resolution and real-time availability checks.

- **Surgery Management**
  - Schedule, search, and manage surgeries.
  - Link surgeries to doctors and patients for streamlined record-keeping.

- **Billing**
  - Automated billing with support for various services like tests, drugs, surgeries, and more.

- **Drug Inventory**
  - Add and update drug stock, view available drugs, and track prescriptions.

- **Test Management**
  - Schedule and manage tests with detailed patient data.

- **Room and Bed Allocation**
  - View and allocate beds dynamically.

---

## Technologies Used

- **Python**: For building the application logic.
- **MySQL**: For database management.
- **Tabulate**: For pretty table formatting in CLI.

---

## Prerequisites

1. Python 3.x installed on your system.
2. MySQL Server running and configured.
3. Required Python libraries:
   - `mysql-connector-python`
   - `tabulate`
   - `datetime`

Install dependencies using:
```
pip install mysql-connector-python tabulate
```

## HOW TO GET IT WORKING
1. Create a database named 'hospital' in you MySQL Server by using this command in the MySQL Command Line:
   ```
   create database hsopital
   ```
2. Download the [hospital.sql](https://github.com/Phoenixfx7/Hospital-Management-System/blob/main/hospital.sql) and [hospital.py](https://github.com/Phoenixfx7/Hospital-Management-System/blob/main/hospital.py) files.

3. Copy the database to your MySQL server by running this in command prompt:
   ```
   mysql -u root -p hospital < hospital.sql
   ```
   **Note:**
   - You'll have to replace root with your MySQL username. (It is root by default if you havent changed it)
   - ```hospital.sql``` must be present in the same directory where command prompt is running
   - MySQL needs to be added to Path (environment variables).
   - You'll be asked for your MySQL password after you run the command. Enter it and its done!



4. You'll need to replace ``` your_username ``` and ``` your_password ``` with your MySQL username and password respectively in the ``` hospital.py ``` file in the statement (Line 10):
```
con=ms.connect(user="your_username",passwd="your_password",host="localhost",database="hospital")
```

5. Run ```hsopital.py```!
---
## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
