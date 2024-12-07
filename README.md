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
```bash
pip install mysql-connector-python tabulate

