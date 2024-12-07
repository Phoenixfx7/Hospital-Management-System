import mysql.connector as ms
from tabulate import tabulate
from datetime import datetime
from datetime import date
from datetime import timedelta
import math
import sys

con=ms.connect(user="your_username",passwd="your_password",host="localhost",database="your_database_name")
cur=con.cursor()

def view_patients():
    header=["Patient_ID","Name","Age","Sex","Phone","Address","Bed_ID", "Admission_Date","Discharge_Date", "Condition","Diagnosis", "Doctor_ID"]
    query="select* from patient"
    cur.execute(query)
    data=cur.fetchall()
    if len(data)==0:
        print("No Patients admitted at the moment...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data,headers=header,tablefmt="simple_grid"))

def view_medics():
    header=["Doctor_ID", "Name", "Specialization", "Phone","Fee","Working Hours","Appointments","Join_Date","Resig_Date"]
    query="select* from medics"
    cur.execute(query)
    data=cur.fetchall()
    if len(data)==0:
        print("No Medics Available")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data,headers=header,tablefmt="simple_grid"))

def view_bills():
    header=["Bill_ID","Patient ID","Patient Name","Date","Rent","Consulation","Tests","Medicines","Misc","Surgery","Tax","Discount","Net"]
    query="select* from bill"
    cur.execute(query)
    data=cur.fetchall()
    if len(data)==0:
        print("No Bills Found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data,headers=header,tablefmt="simple_grid"))

def view_cost():
    header = ["Name", "Service_Type", "Price"]
    query = "SELECT * FROM cost"
    cur.execute(query)
    data = cur.fetchall()
    if len(data) == 0:
        print("No cost records found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data, headers=header, tablefmt="simple_grid"))

def view_beds():
    header = ["Bed_ID", "Type", "Room", "Floor", "Occupied", "Patient_ID"]
    query = "SELECT * FROM beds"
    cur.execute(query)
    data = cur.fetchall()
    if len(data) == 0:
        print("No bed records found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data, headers=header, tablefmt="simple_grid"))

def view_tests():
    header = ["Test_ID", "Patient_ID", "Date_Time", "Name", "Cost", "Remarks"]
    query = "SELECT * FROM tests"
    cur.execute(query)
    data = cur.fetchall()
    if len(data) == 0:
        print("No test records found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data, headers=header, tablefmt="simple_grid"))

def view_appointments():
    header = ["Appointment_ID","Doctor_ID", "Doctor_Name", "Date", "Start_Time", "End_Time",  "Patient_ID", "Patient_Name"]
    query = "SELECT * FROM appointments"
    cur.execute(query)
    data = cur.fetchall()
    if len(data) == 0:
        print("No appointments found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data, headers=header, tablefmt="simple_grid"))

def view_allocation():
    header = ["Patient_ID", "Bed_ID", "Start_DateTime", "End_DateTime", "Type"]
    query = "SELECT * FROM allocation"
    cur.execute(query)
    data = cur.fetchall()
    if len(data) == 0:
        print("No allocation records found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data, headers=header, tablefmt="simple_grid"))

def view_drugs():
    header = ["Drug_ID", "Name", "Price", "Manufacturer", "Side_Effect_1", "Side_Effect_2", "Stock"]
    query = "SELECT * FROM drugs"
    cur.execute(query)
    data = cur.fetchall()
    if len(data) == 0:
        print("No drug records found...")
    else:
        print(f"{len(data)} Records Found: \n")
        print(tabulate(data, headers=header, tablefmt="simple_grid"))

def search_patient():
    print("Search Patient Records by:")
    print("1. ID")
    print("2. Name")
    print("3. Age ")
    print("4. Sex ")
    print("5. Phone")
    print("6. Address")
    print("7. Doctor Name")
    print("8. Doctor ID")
    print("9. Bed ID")
    print("10. Date of Admission ")
    print("11. Date of Discharge")
    print("12. Medical Condition )")
    print("13. Diagnosis")
    choice = input("Enter your choice (1-13): ")

    query = "SELECT * FROM patient WHERE"
    conditions=""

    if choice == '1':  # Search by ID
        patient_id = input("Enter Patient ID: ")
        conditions=(f" id LIKE '%{patient_id}%' ")

    elif choice == '2':  # Search by Name
        name = input("Enter Patient Name: ")
        conditions=(f" name LIKE '%{name}%' ")

    elif choice == '3':  # Search by Age
        age_choice = input("Search by (1) Exact Age or (2) Age Range: ")
        if age_choice == '1':
            age = input("Enter Exact Age: ")
            conditions=(f" a LIKE '%{age}%' ")
        elif age_choice == '2':
            age_min = input("Enter Minimum Age: ")
            age_max = input("Enter Maximum Age: ")
            conditions=(f" a BETWEEN {age_min} AND {age_max} ")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return search_patient()

    elif choice == '4':  # Search by Sex
        print("Select Gender: \n1. Male\t2. Female")
        sex_choice = input("Enter choice (1 or 2): ")
        if sex_choice == '1':
            conditions=(f" s LIKE '%M%' ")
        elif sex_choice == '2':
            conditions=(f" s LIKE '%F%' ")
        else:
            print("Invalid choice. Please select 1 or 2.")
            return search_patient()

    elif choice == '5':  # Search by Phone
        phone = input("Enter Phone Number: ")
        conditions=(f" phone LIKE '%{phone}%' ")

    elif choice == '6':  # Search by Address
        address = input("Enter Address: ")
        conditions=(f" addr LIKE '%{address}%' ")

    elif choice == '7':  # Search by Doctor Name
        doctor_name = input("Enter Doctor Name: ")
        conditions=(f" diag LIKE '%{doctor_name}%' ")

    elif choice == '8':  # Search by Doctor ID
        doctor_id = input("Enter Doctor ID: ")
        conditions=(f" did LIKE '%{doctor_id}%' ")

    elif choice == '9':  # Search by Bed ID
        bed_id = input("Enter Bed ID: ")
        conditions=(f" bid LIKE '%{bed_id}%' ")

    elif choice == '10':  # Search by Date of Admission
        date_choice = input("Search by (1) Exact Date or (2) Date Range: ")
        if date_choice == '1':
            doa = input("Enter Date of Admission (YYYY-MM-DD): ")
            conditions=(f" doa LIKE '{doa}%' ")
        elif date_choice == '2':
            doa_start = input("Enter Start Date of Admission (YYYY-MM-DD): ")
            doa_end = input("Enter End Date of Admission (YYYY-MM-DD): ")
            conditions=(f" doa BETWEEN '{doa_start}' AND '{doa_end}' ")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return search_patient()

    elif choice == '11':  # Search by Date of Discharge
        date_choice = input("Search by (1) Exact Date or (2) Date Range: ")
        if date_choice == '1':
            dod = input("Enter Date of Discharge (YYYY-MM-DD): ")
            conditions=(f" dod LIKE '{dod}%' ")
        elif date_choice == '2':
            dod_start = input("Enter Start Date of Discharge (YYYY-MM-DD): ")
            dod_end = input("Enter End Date of Discharge (YYYY-MM-DD): ")
            conditions=(f" dod BETWEEN '{dod_start}' AND '{dod_end}' ")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return search_patient()

    elif choice == '12':  # Search by Medical Condition
        print("Select Medical Condition: \n1. Mild\t2. Severe\t3. Extreme\t4. Dead")
        condition_choice = input("Enter choice (1-4): ")
        if condition_choice == '1':
            conditions=(f" cond LIKE '%Mild%' ")
        elif condition_choice == '2':
            conditions=(f" cond LIKE '%Severe%' ")
        elif condition_choice == '3':
            conditions=(f" cond LIKE '%Extreme%' ")
        elif condition_choice == '4':
            conditions=(f" cond LIKE '%Dead%' ")
        else:
            print("Invalid choice. Please select a valid option (1-4).")
            return search_patient()

    elif choice == '13':  # Search by Diagnosis
        diagnosis = input("Enter Diagnosis: ")
        conditions=(f" diag LIKE '%{diagnosis}%' ")

    else:
        print("Invalid choice. Please enter a number between 1 and 13.")
        return search_patient()

    # Combine the conditions with 'AND' and form the final query
    if conditions:
        query+=" "+conditions
    
    # Execute the query
    cur.execute(query)
    results = cur.fetchall()
    headers = ["ID", "Name", "Age", "Sex", "Phone", "Address", "Bed ID", "Date of Admission", 
               "Date of Discharge", "Medical Condition", "Diagnosis", "Doctor ID"]

    if results:
        print(f"{len(results)} Records Found: \n")
        print(tabulate(results, headers=headers, tablefmt="simple_grid"))
    else:
        print("No records found.")

def search_medic():
    while True:
        print("\nSearch Medics:")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Search by Specialization")
        print("4. Search by Phone")
        print("5. Search by Work (Day of the week or Date)")
        print("6. Search by Appointments (Date)")

        choice = input("Enter your choice: ")
        query = "SELECT * FROM medics WHERE"
        conditions = ""

        # Search by ID
        if choice == "1":
            med_id = int(input("Enter ID: "))
            conditions=(f"id like '%{med_id}%'")
        
        # Search by Name
        elif choice == "2":
            name = input("Enter Name: ")
            conditions=(f"name LIKE '%{name}%'")
        
        # Search by Specialization
        elif choice == "3":
            spec = input("Enter Specialization: ")
            conditions=(f"spec LIKE '%{spec}%'")
        
        # Search by Phone
        elif choice == "4":
            phone = input("Enter Phone: ")
            conditions=(f"ph LIKE '%{phone}%'")
        
        # Search by Work (Day of the week or Date)
        elif choice == "5":
            work_choice = input("Search by Day of the week (1) or Date (2): ")
            
            if work_choice == "1":
                print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday")
                while True:
                    day_choice = input("Enter Day of the week (1-7): ")
                    days_of_week = {
                        "1": "Mon", "2": "Tue", "3": "Wed", "4": "Thu", "5": "Fri", "6": "Sat", "7": "Sun"
                    }
                    day = days_of_week.get(day_choice)
                    if day:
                        conditions=(f"work LIKE '%{day}%'")
                        break
                    else:
                        print("Invalid day choice. Please enter a valid day (1-7).")
            
            elif work_choice == "2":
                while True:
                    work_date = input("Enter Date (YYYY-MM-DD): ")
                    try:
                        date_obj = datetime.strptime(work_date, "%Y-%m-%d")
                        day_of_week = date_obj.strftime("%a")  # Get the day abbreviation (Mon, Tue, etc.)
                        conditions=(f"work LIKE '%{day_of_week}%'")
                        break
                    except ValueError:
                        print("Invalid date format. Please enter a valid date (YYYY-MM-DD).")
            else:
                print("Invalid choice. Please select either 1 (for Day of the week) or 2 (for Date).")
                continue
        
        # Search by Appointments (Date)
        elif choice == "6":
            while True:
                appt_date = input("Enter Appointment Date (YYYY-MM-DD): ")
                try:
                    conditions=(f"appts LIKE '%{appt_date}%'")
                    break
                except ValueError:
                    print("Invalid date format. Please enter a valid date (YYYY-MM-DD).")
        
        # If invalid choice entered
        else:
            print("Invalid choice. Please enter a valid option (1-6).")
            continue
        
        query += " "+conditions
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("No matching records found.")
        else:
            print(f"{len(result)} Records Found: \n")
            headers = ["ID", "Name", "Specialization", "Phone","Fee", "Work", "Appointments","Joining Date", "Resignation Date"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))

        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search_surgery():
    while True:
        print("\nSearch Surgery:")
        print("1. Search by Surgery Name")
        print("2. Search by Patient ID")
        print("3. Search by Patient Name")
        print("4. Search by Doctor ID")
        print("5. Search by Doctor Name")
        print("6. Search by Surgery Date (Exact or Range)")
        choice = input("Enter your choice: ")
        query = "SELECT * FROM surgery WHERE"
        conditions=""

        if choice == "1":
            surgery_name = input("Enter Surgery Name: ").strip()
            conditions=(f"name LIKE '%{surgery_name}%'")
        elif choice == "2":
            patient_id = input("Enter Patient ID: ").strip()
            conditions=(f"pid LIKE '%{patient_id}%'")
        elif choice == "3":
            patient_name = input("Enter Patient Name: ").strip()
            conditions=(f"pname LIKE '%{patient_name}%'")
        elif choice == "4":
            doctor_id = input("Enter Doctor ID: ").strip()
            conditions=(f"did LIKE '%{doctor_id}%'")
        elif choice == "5":
            doctor_name = input("Enter Doctor Name: ").strip()
            conditions=(f"dname LIKE '%{doctor_name}%'")
        elif choice == "6":
            date_choice = input("Search by Exact Date (1) or Date Range (2): ")
            if date_choice == "1":
                surgery_date = input("Enter Surgery Date (YYYY-MM-DD): ").strip()
                conditions=(f"date = '{surgery_date}'")
            elif date_choice == "2":
                start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
                end_date = input("Enter End Date (YYYY-MM-DD): ").strip()
                conditions=(f"date BETWEEN '{start_date}' AND '{end_date}'")
            else:
                print("Invalid choice. Please select either 1 (Exact Date) or 2 (Date Range).")
                continue
        else:
            print("Invalid choice. Please enter a valid option (1-6).")
            continue

        query+=" "+conditions
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("No matching records found.")
        else:
            print(f"\n{len(result)} Record(s) Found:\n")
            headers = ["Surgery Name", "Date", "Patient ID", "Patient Name", "Doctor ID", "Doctor Name"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))

        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search_bill():
    while True:
        print("\nSearch Bill:")
        print("1. Search by Bill ID")
        print("2. Search by Patient ID")
        print("3. Search by Patient Name")
        print("4. Search by Billing Date (Exact or Range)")
        choice = input("Enter your choice: ")
        query = "SELECT * FROM bill WHERE"
        conditions=""
        # Search by Bill ID
        if choice == "1":
            bill_id = input("Enter Bill ID: ")
            conditions=(f"id LIKE '%{bill_id}%'")
        # Search by Patient ID
        elif choice == "2":
            patient_id = input("Enter Patient ID: ")
            conditions=(f"pid LIKE '%{patient_id}%'")
        # Search by Patient Name
        elif choice == "3":
            pname = input("Enter Patient Name: ")
            conditions=(f"pname LIKE '%{pname}%'")
        # Search by Billing Date (Exact or Range)
        elif choice == "4":
            date_choice = input("Search by Exact Date (1) or Date Range (2): ")
            if date_choice == "1":
                bill_date = input("Enter Billing Date (YYYY-MM-DD): ")
                conditions=(f"date LIKE '{bill_date}'")
            elif date_choice == "2":
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                conditions=(f"date BETWEEN '{start_date}' AND '{end_date}'")
            else:
                print("Invalid choice. Please select either 1 (for Exact Date) or 2 (for Date Range).")
                continue

        else:
            print("Invalid choice. Please enter a valid option (1-4).")
            continue

        query+=" "+conditions
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("No matching records found.")
        else:
            print(f"{len(result)} Records Found: \n")
            headers = ["Bill ID", "Patient ID", "Patient Name", "Billing Date", "Rent", "Cons", "Food", "Test", "Drugs", "Prof", "Tax", "Discount", "Net"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))

        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search_services():
    while True:
        print("\nSearch Services:")
        print("1. Search by Service Name")
        print("2. Search by Service Type")
        print("3. Search by Price Range")
        choice = input("Enter your choice: ")
        query = "SELECT * FROM cost WHERE"
        conditions=""

        if choice == "1":
            service_name = input("Enter Service Name: ").strip()
            conditions=(f"name LIKE '%{service_name}%'")
        elif choice == "2":
            service_type = input("Enter Service Type (e.g., Test, Room, Surgery): ").strip()
            conditions=(f"stype LIKE '%{service_type}%'")
        elif choice == "3":
            min_price = input("Enter Minimum Price: ").strip()
            max_price = input("Enter Maximum Price: ").strip()
            if min_price.isdigit() and max_price.isdigit():
                conditions=(f"price BETWEEN {min_price} AND {max_price}")
            else:
                print("Invalid price range. Please enter valid numeric values.")
                continue
        else:
            print("Invalid choice. Please enter a valid option (1-3).")
            continue

        query+=" "+conditions
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("No matching records found.")
        else:
            print(f"\n{len(result)} Record(s) Found:\n")
            headers = ["Service Name", "Service Type", "Price"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))

        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search_drugs():
    while True:
        print("\nSearch Drugs:")
        print("1. Search by Drug ID")
        print("2. Search by Drug Name")
        print("3. Search by Manufacturer")
        print("4. Search by Short Composition (sc1 or sc2)")
        print("5. Search by Stock (Range)")
        choice = input("Enter your choice: ")
        query = "SELECT * FROM drugs WHERE"
        conditions=""
        if choice == "1":
            drug_id = input("Enter Drug ID: ")
            conditions=(f"id LIKE '%{drug_id}%'")
        elif choice == "2":
            drug_name = input("Enter Drug Name: ")
            conditions=(f"name LIKE '%{drug_name}%'")
        elif choice == "3":
            manufacturer = input("Enter Manufacturer: ")
            conditions=(f"mfg LIKE '%{manufacturer}%'")
        elif choice == "4":
            short_comp = input("Enter Short Composition (sc1 or sc2): ")
            conditions=(f"sc1 LIKE '%{short_comp}%' OR sc2 LIKE '%{short_comp}%'")
        elif choice == "5":
            while True:
                try:
                    stock_min = int(input("Enter minimum stock: "))
                    stock_max = int(input("Enter maximum stock: "))
                    conditions=(f"stock BETWEEN {stock_min} AND {stock_max}")
                    break
                except ValueError:
                    print("Invalid input. Please enter valid integers for stock.")
        else:
            print("Invalid choice. Please enter a valid option (1-5).")
            continue
        query+=" "+conditions
        query += ";"
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("No matching records found.")
        else:
            print(f"{len(result)} Records Found: \n")
            headers = ["Drug ID", "Drug Name", "Price", "Manufacturer", "Short Composition 1", "Short Composition 2", "Stock"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))
        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search_tests():
    while True:
        print("\nSearch Tests:")
        print("1. Search by Test ID")
        print("2. Search by Patient ID")
        print("3. Search by Test Date (Exact or Range)")
        print("4. Search by Test Name")
        choice = input("Enter your choice: ")
        query = "SELECT * FROM tests WHERE"
        conditions=""
        if choice == "1":
            test_id = input("Enter Test ID: ")
            conditions=(f"id LIKE '%{test_id}%'")
        elif choice == "2":
            patient_id = input("Enter Patient ID: ")
            conditions=(f"pid LIKE '%{patient_id}%'")
        elif choice == "3":
            date_choice = input("Search by Exact Date (1) or Date Range (2): ")
            if date_choice == "1":
                test_date = input("Enter Test Date (YYYY-MM-DD): ")
                conditions=(f"dt LIKE '{test_date}%'")
            elif date_choice == "2":
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                conditions=(f"dt BETWEEN '{start_date}' AND '{end_date}'")
            else:
                print("Invalid choice. Please select either 1 (for Exact Date) or 2 (for Date Range).")
                continue
        elif choice == "4":
            test_name = input("Enter Test Name: ")
            conditions=(f"name LIKE '%{test_name}%'")
        else:
            print("Invalid choice. Please enter a valid option (1-4).")
            continue
        query+=" "+conditions
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("No matching records found.")
        else:
            print(f"{len(result)} Records Found: \n")
            headers = ["Test ID", "Patient ID", "Test Date", "Test Name"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))
        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search_appointments():
    while True:
        print("\nSearch Appointments:")
        print("1. Search by Appointment ID")
        print("2. Search by Doctor ID")
        print("3. Search by Doctor Name")
        print("4. Search by Patient ID")
        print("5. Search by Patient Name")
        print("6. Search by Appointment Date (Exact or Range)")
        print("7. Search by Status (1. Scheduled, 2. Completed, 3. Cancelled)")
        choice = input("Enter your choice: ")
        query = "SELECT * FROM appointments WHERE"
        conditions=""

        if choice == "1":
            appointment_id = input("Enter Appointment ID: ")
            conditions=(f"id LIKE '%{appointment_id}%'")
        elif choice == "2":
            doctor_id = input("Enter Doctor ID: ")
            conditions=(f"did LIKE '%{doctor_id}%'")
        elif choice == "3":
            doctor_name = input("Enter Doctor Name: ")
            conditions=(f"dname LIKE '%{doctor_name}%'")
        elif choice == "4":
            patient_id = input("Enter Patient ID: ")
            conditions=(f"pid LIKE '%{patient_id}%'")
        elif choice == "5":
            patient_name = input("Enter Patient Name: ")
            conditions=(f"pname LIKE '%{patient_name}%'")
        elif choice == "6":
            date_choice = input("Search by Exact Date (1) or Date Range (2): ")
            if date_choice == "1":
                appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
                conditions=(f"date LIKE '{appointment_date}%'")
            elif date_choice == "2":
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                conditions=(f"date BETWEEN '{start_date}' AND '{end_date}'")
            else:
                print("Invalid choice. Please select either 1 (for Exact Date) or 2 (for Date Range).")
                continue
        elif choice == "7":
            print("\nStatus Options:")
            print("1. Scheduled")
            print("2. Completed")
            print("3. Cancelled")
            status_choice = input("Enter your choice: ")
            status_map = {"1": "Scheduled", "2": "Completed", "3": "Cancelled"}
            status = status_map.get(status_choice)
            if not status:
                print("Invalid status choice. Please try again.")
                continue
            conditions=(f"status LIKE '%{status}%'")
        else:
            print("Invalid choice. Please enter a valid option (1-7).")
            continue

        query+=" "+conditions
        cur.execute(query)
        result = cur.fetchall()

        if not result:
            print("No matching records found.")
        else:
            print(f"{len(result)} Records Found: \n")
            headers = ["Appointment ID", "Date", "Doctor ID", "Doctor Name", "Patient ID", "Patient Name", "Status"]
            print(tabulate(result, headers=headers, tablefmt="simple_grid"))

        search_again = input("\nDo you want to search again? (y/n): ").strip().lower()
        if search_again != 'y':
            print("Exiting search.")
            break

def search():
    while True:
        print("\nSearch Menu:")
        print("1. Search Patients")
        print("2. Search Doctors")
        print("3. Search Tests")
        print("4. Search Appointments")
        print("5. Search Drugs")
        print("6. Search Bills")
        print("7. Search Surgeries")
        print("8. Search Services")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            search_patient()
        elif choice == "2":
            search_medic()
        elif choice == "3":
            search_tests()
        elif choice == "4":
            search_appointments()
        elif choice == "5":
            search_drugs()
        elif choice == "6":
            search_bill()
        elif choice=="7":
            search_surgery()
        elif choice=="8":
            search_services()
        elif choice == "9":
            print("Exiting search menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")

def view():
    while True:
        print("\nView Menu:")
        print("1. View Patients")
        print("2. View Doctors")
        print("3. View Beds")
        print("4. View Bills")
        print("5. View Drugs")
        print("6. View Tests")
        print("7. View Allocations")
        print("8. View Appointments")
        print("9. View Costs")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_patients()
        elif choice == "2":
            view_medics()
        elif choice == "3":
            view_beds()
        elif choice == "4":
            view_bills()
        elif choice == "5":
            view_drugs()
        elif choice == "6":
            view_tests()
        elif choice == "7":
            view_allocation()
        elif choice == "8":
            view_appointments()
        elif choice == "9":
            view_cost()
        elif choice == "10":
            print("Exiting view menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-10).")

def admit_patient():
    while True:
        print("\nAdmit Patient")
        print("1. Admit Existing Patient")
        print("2. Create New Patient Entry")
        while True:
            choice = input("Enter your choice: ").strip()
            if choice in {"1", "2"}:
                break
            print("Invalid choice. Please enter 1 or 2.")

        if choice == "1":  # Admit Existing Patient
            while True:
                pid = input("Enter Patient ID: ").strip()
                cur.execute("SELECT * FROM patient WHERE id = %s", (pid,))
                existing_patient = cur.fetchone()
                if not existing_patient:
                    print("Patient ID not found. Please try again.")
                    continue
                if existing_patient[6] is not None:  # Check if already assigned a bed
                    print("Patient is already admitted. Please check details.")
                    continue
                break

            print("\nPatient Details:")
            print(tabulate([existing_patient], headers=["ID", "Name", "Age", "Sex", "Phone", "Address", "Bed ID", "DOA", "DOD", "Condition", "Diagnosis", "Doc_ID"], tablefmt="simple_grid"))

            while True:
                bed_id = input("Enter Bed ID: ").strip().upper()
                cur.execute("SELECT * FROM beds WHERE bid = %s", (bed_id,))
                bed = cur.fetchone()
                if not bed:
                    print("Bed ID not found. Please try again.")
                    continue
                if bed[4] == "Yes":
                    print("Bed is already occupied. Please select a different bed.")
                    continue
                break

            print("\n1. Mild\n2. Severe\n3. Extreme")
            while True:
                condition_choice = input("Select Condition: ").strip()
                if condition_choice in {"1", "2", "3"}:
                    condition = {"1": "Mild", "2": "Severe", "3": "Extreme"}[condition_choice]
                    break
                print("Invalid choice for condition. Please try again.")

            diag = input("Enter Diagnosis/Reason for Admission: ").strip()

            admission_date = date.today()

            cur.execute(
                "UPDATE patient SET bid = %s, doa = %s, dod = NULL, cond = %s, diag = %s WHERE id = %s",
                (bed_id, admission_date, condition, diag, pid),
            )
            cur.execute("UPDATE beds SET occupied = 'Yes', pid = %s WHERE bid = %s", (pid, bed_id))
            cur.execute("INSERT INTO allocation (pid, bid, start, end) VALUES (%s, %s, NOW(), NULL)", (pid, bed_id))

            cur.execute("SELECT * FROM patient WHERE id = %s", (pid,))
            updated_patient = cur.fetchall()

            print("\nPreview of Updated Patient Details:")
            print(tabulate(updated_patient, headers=["ID", "Name", "Age", "Sex", "Phone", "Address", "Bed ID", "DOA", "DOD", "Condition", "Diagnosis", "Doc_ID"], tablefmt="simple_grid"))

        elif choice == "2":  # Create New Patient Entry
            name = input("Enter Patient Name: ").strip()
            while True:
                age = input("Enter Age: ").strip()
                if age.isdigit():
                    break
                print("Invalid Age. Please enter a valid number.")

            print("\n1. Male\n2. Female")
            while True:
                sex_choice = input("Select Gender: ").strip()
                if sex_choice in {"1", "2"}:
                    sex = "M" if sex_choice == "1" else "F"
                    break
                print("Invalid choice for gender. Please try again.")

            while True:
                phone = input("Enter Phone Number (10 digits): ").strip()
                if phone.isdigit() and len(phone) == 10:
                    break
                print("Invalid phone number. Please enter a 10-digit number.")

            addr = input("Enter Address: ").strip()

            while True:
                bed_id = input("Enter Bed ID: ").strip().upper()
                cur.execute("SELECT * FROM beds WHERE bid = %s", (bed_id,))
                bed = cur.fetchone()
                if not bed:
                    print("Bed ID not found. Please try again.")
                    continue
                if bed[4] == "Yes":
                    print("Bed is already occupied. Please select a different bed.")
                    continue
                break

            print("\n1. Mild\n2. Severe\n3. Extreme")
            while True:
                condition_choice = input("Select Condition: ").strip()
                if condition_choice in {"1", "2", "3"}:
                    condition = {"1": "Mild", "2": "Severe", "3": "Extreme"}[condition_choice]
                    break
                print("Invalid choice for condition. Please try again.")

            diag = input("Enter Diagnosis/Reason for Admission: ").strip()

            while True:
                doctor_id = input("Enter Doctor ID: ").strip()
                cur.execute("SELECT * FROM medics WHERE id = %s and dor is null", (doctor_id,))
                doctor = cur.fetchone()
                if not doctor:
                    print("Doctor ID not found. Please try again.")
                    continue
                break

            admission_date = date.today()

            cur.execute(
                "INSERT INTO patient (name, a, s, phone, addr, bid, doa, dod, cond, diag, did) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, NULL, %s, %s, %s)",
                (name, age, sex, phone, addr, bed_id, admission_date, condition, diag, doctor_id),
            )

            cur.execute("UPDATE beds SET occupied = 'Yes', pid = LAST_INSERT_ID() WHERE bid = %s", (bed_id,))
            cur.execute("INSERT INTO allocation (pid, bid, start, end) VALUES (LAST_INSERT_ID(), %s, NOW(), NULL)", (bed_id,))

            cur.execute("SELECT * FROM patient WHERE id = LAST_INSERT_ID()")
            latest_patient = cur.fetchall()

            print("\nPreview of New Patient Details:")
            print(tabulate(latest_patient, headers=["ID", "Name", "Age", "Sex", "Phone", "Address", "Bed ID", "DOA", "DOD", "Condition", "Diagnosis", "Doc_ID"], tablefmt="simple_grid"))

        confirm = input("\nDo you want to confirm the admission? (y/n): ").strip().lower()
        if confirm == 'y':
            con.commit()
            print("\nPatient admitted successfully!")
        else:
            con.rollback()
            print("\nAdmission cancelled.")

        admit_another = input("\nDo you want to admit another patient? (y/n): ").strip().lower()
        if admit_another != 'y':
            print("Exiting admission process.")
            break

def add_medics():
    while True:
        print("\nAdd New Medic")
        name = input("Enter Medic Name: ").strip()
        spec = input("Enter Specialization: ").strip()

        while True:
            phone = input("Enter Phone Number (10 digits): ").strip()
            if phone.isdigit() and len(phone) == 10:
                break
            print("Invalid phone number. Please enter a 10-digit number.")

        while True:
            fee = input("Enter Consultation Fee: ").strip()
            if fee.isdigit() and int(fee) >= 0:
                fee = int(fee)
                break
            print("Invalid fee. Please enter a non-negative number.")

        print("\nEnter Working Hours (leave blank if holiday):")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        work_hours = []

        for day in days:
            while True:
                start_time = input(f"Enter Start Time for {day} (HH:MM, leave blank if holiday): ").strip()
                end_time = input(f"Enter End Time for {day} (HH:MM, leave blank if holiday): ").strip()

                if not start_time and not end_time:  # Holiday
                    break

                if start_time and end_time:  # Both times provided
                    try:
                        start_dt = datetime.strptime(start_time, "%H:%M")
                        end_dt = datetime.strptime(end_time, "%H:%M")
                        if end_dt > start_dt:
                            work_hours.append(f"{day[:3]}, {start_time}-{end_time}")
                            break
                        else:
                            print("End time must be later than start time. Please re-enter.")
                    except ValueError:
                        print("Invalid time format. Please enter in HH:MM format.")
                else:
                    print("Both start and end time must be provided or leave both blank for a holiday.")

        work = "\n".join(work_hours)
        doj = date.today()

        cur.execute(
            "INSERT INTO medics (name, spec, ph, fee, work, appts, doj, dor) "
            "VALUES (%s, %s, %s, %s, %s, NULL, %s, NULL)",
            (name, spec, phone, fee, work, doj),
        )

        cur.execute("SELECT * FROM medics WHERE id = LAST_INSERT_ID()")
        latest_medic = cur.fetchall()

        print("\nPreview of New Medic:")
        print(tabulate(latest_medic, headers=["ID", "Name", "Specialization", "Phone", "Fee", "Work Hours", "Appointments", "Date of Joining", "Date of Retirement"], tablefmt="simple_grid"))

        confirm = input("\nDo you want to confirm the addition? (y/n): ").strip().lower()
        if confirm == 'y':
            con.commit()
            print("\nMedic added successfully!")
        else:
            con.rollback()
            print("\nAddition cancelled.")

        add_another = input("\nDo you want to add another medic? (y/n): ").strip().lower()
        if add_another != 'y':
            print("Exiting medic addition process.")
            break

def add_appointments():
    while True:
        print("\nAdd New Appointment")
        print("1. Book for Existing Patient")
        print("2. Book for New Patient")
        while True:
            choice = input("Enter your choice: ").strip()
            if choice in {"1", "2"}:
                break
            print("Invalid choice. Please enter 1 or 2.")

        while True:
            doctor_id = input("Enter Doctor ID: ").strip()
            cur.execute("SELECT * FROM medics WHERE id = %s and dor is null", (doctor_id,))
            doctor = cur.fetchone()
            if not doctor:
                print("Doctor ID not found. Please try again.")
                continue
            break
        doctor_name = doctor[1]

        while True:
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
            try:
                appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
                day_of_week = appointment_date.strftime("%A")[:3]
                break
            except ValueError:
                print("Invalid date format. Please try again.")

        available_slots = []
        doctor_schedule = doctor[5]
        if day_of_week in doctor_schedule:
            for entry in doctor_schedule.split("\n"):
                if entry.startswith(day_of_week):
                    times = entry.split(",")[1].strip()
                    available_slots = [slot.strip() for slot in times.split("-")]
                    break
        if not available_slots:
            print(f"The doctor is not available on {day_of_week}. Please select another day.")
            continue

        while True:
            start_time = input(f"Enter Start Time (HH:MM, Available: {available_slots[0]} to {available_slots[1]}): ").strip()
            end_time = input("Enter End Time (HH:MM): ").strip()
            try:
                start_time_obj = datetime.strptime(start_time, "%H:%M").time()
                end_time_obj = datetime.strptime(end_time, "%H:%M").time()
                if start_time_obj >= end_time_obj or start_time_obj < datetime.strptime(available_slots[0], "%H:%M").time() or end_time_obj > datetime.strptime(available_slots[1], "%H:%M").time():
                    print("Invalid time slot. Please enter valid start and end times within the available range.")
                    continue

                cur.execute(
                    "SELECT * FROM appointments WHERE did = %s AND date = %s AND (start < %s AND end > %s)",
                    (doctor_id, appointment_date, end_time, start_time),)
                conflicting_appointment = cur.fetchone()
                if conflicting_appointment:
                    print("The selected time slot conflicts with another appointment. Please try a different time.")
                    continue
                break
            except ValueError:
                print("Invalid time format. Please try again.")

        if choice == "1":
            while True:
                patient_id = input("Enter Patient ID: ").strip()
                cur.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
                patient = cur.fetchone()
                if not patient:
                    print("Patient ID not found. Please try again.")
                    continue
                break
            patient_name = patient[1]

        elif choice == "2":
            patient_name = input("Enter Patient Name: ").strip()
            while True:
                age = input("Enter Age: ").strip()
                if age.isdigit():
                    break
                print("Invalid Age. Please enter a valid number.")
            print("\n1. Male\n2. Female")
            while True:
                sex_choice = input("Select Gender: ").strip()
                if sex_choice in {"1", "2"}:
                    sex = "M" if sex_choice == "1" else "F"
                    break
                print("Invalid choice for gender. Please try again.")
            while True:
                phone = input("Enter Phone Number (10 digits): ").strip()
                if phone.isdigit() and len(phone) == 10:
                    break
                print("Invalid phone number. Please enter a 10-digit number.")
            address = input("Enter Address: ").strip()
            cur.execute(
                "INSERT INTO patient (name, a, s, phone, addr, did) VALUES (%s, %s, %s, %s, %s, %s)",
                (patient_name, age, sex, phone, address, doctor_id),)
            patient_id = cur.lastrowid

        cur.execute(
            "INSERT INTO appointments (did, dname, date, start, end, pid, pname, status) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, 'Scheduled')",
            (doctor_id, doctor_name, appointment_date, start_time, end_time, patient_id, patient_name),)

        appointment_id = cur.lastrowid
        cur.execute("SELECT * FROM appointments WHERE id = %s", (appointment_id,))
        latest_appointment = cur.fetchall()

        print("\nPreview of Appointment Details:")
        print(tabulate(latest_appointment, headers=["ID", "Doctor ID", "Doctor Name", "Date", "Start Time", "End Time", "Patient ID", "Patient Name", "Status"], tablefmt="simple_grid"))

        confirm = input("\nDo you want to confirm this appointment? (y/n): ").strip().lower()
        if confirm == 'y':
            appointment_entry = f"{appointment_date}, {start_time} - {end_time}"
            if doctor[6]:
                new_appts = doctor[6] + "\n" + appointment_entry
            else:
                new_appts = appointment_entry
            cur.execute("UPDATE medics SET appts = %s WHERE id = %s", (new_appts, doctor_id))
            con.commit()
            print("\nAppointment booked successfully!")
        else:
            con.rollback()
            print("\nAppointment booking cancelled.")

        book_another = input("\nDo you want to book another appointment? (y/n): ").strip().lower()
        if book_another != 'y':
            print("Exiting appointment booking process.")
            break

def add_services():
    while True:
        print("\nAdd New Service")
        name = input("Enter Service Name: ")
        print("\nService Types:")
        print("1. Test")
        print("2. Room")
        print("3. Surgery")
        print("4. Misc.")
        while True:
            stype_choice = input("Select Service Type: ").strip()
            if stype_choice in {"1", "2", "3", "4"}:
                stype = {"1": "Test", "2": "Room", "3": "Surgery","4":"Misc"}[stype_choice]
                break
            print("Invalid choice. Please select a valid option (1-4).")

        while True:
            price = input("Enter Price: ").strip()
            if price.isdigit():
                price = int(price)
                break
            print("Invalid price. Please enter a numeric value.")
        query = "INSERT INTO cost (name, stype, price) VALUES ('{}', '{}', {});".format(name, stype, price)
        cur.execute(query)
        cur.execute("SELECT * FROM cost WHERE name = '%s' AND stype = '%s' AND price = %s;"%(name, stype, price))
        result = cur.fetchall()

        print("\nPreview of Added Service:")
        print(tabulate(result, headers=["Service Name", "Service Type", "Price"], tablefmt="simple_grid"))

        confirm = input("\nDo you want to confirm the addition? (y/n): ").strip().lower()
        if confirm == 'y':
            con.commit()
            print("\nService added successfully!")
        else:
            con.rollback()
            print("\nService addition cancelled.")

        add_another = input("\nDo you want to add another service? (y/n): ").strip().lower()
        if add_another != 'y':
            print("Exiting service addition process.")
            break

def add_drugs():
    while True:
        print("\nAdd New Drug")
        name = input("Enter Drug Name: ").strip()
        while True:
            price = input("Enter Drug Price: ").strip()
            try:
                price = float(price)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
        mfg = input("Enter Manufacturer Name: ").strip()
        sc1 = input("Enter Short Composition 1: ").strip()
        sc2 = input("Enter Short Composition 2 (optional): ").strip()
        while True:
            stock = input("Enter Stock Quantity: ").strip()
            if stock.isdigit():
                stock = int(stock)
                break
            print("Invalid stock quantity. Please enter a valid number.")
        cur.execute("INSERT INTO drugs (name, price, mfg, sc1, sc2, stock) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, price, mfg, sc1, sc2, stock))
        cur.execute("SELECT * FROM drugs WHERE name = %s AND mfg = %s", (name, mfg))
        result = cur.fetchall()
        print("\nPreview of Added Drug:")
        print(tabulate(result, headers=["ID", "Name", "Price", "Manufacturer", "Composition 1", "Composition 2", "Stock"], tablefmt="simple_grid"))
        confirm = input("\nDo you want to confirm the addition? (y/n): ").strip().lower()
        if confirm == 'y':
            con.commit()
            print("\nDrug added successfully!")
        else:
            con.rollback()
            print("\nDrug addition cancelled.")
        add_another = input("\nDo you want to add another drug? (y/n): ").strip().lower()
        if add_another != 'y':
            print("Exiting drug addition process.")
            break

def add_test():
    while True:
        print("\nAdd New Test:")
        cur.execute("SELECT * FROM cost WHERE stype = 'Test'")
        tests = cur.fetchall()
        if not tests:
            print("No tests available.")
            break
        print("\nAvailable Tests:")
        for idx, test in enumerate(tests, 1):
            print(f"{idx}. {test[0]} - Price: {test[2]}")
        while True:
            choice = input(f"Select Test (1-{len(tests)}): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(tests):
                selected_test = tests[int(choice) - 1]
                test_name = selected_test[0]
                test_price = selected_test[2]
                break
            print("Invalid selection. Please try again.")
        while True:
            pid = input("Enter Patient ID: ").strip()
            if pid.isdigit():
                pid = int(pid)
                break
            print("Invalid Patient ID. Please try again.")
        test_date=input("Enter Test Date(YYYY-MM-DD): ").strip()+" "
        test_time=input("Enter Test Time(HH:MM): ").strip()
        test_datetime=test_date+test_time
        cur.execute(
            "INSERT INTO tests (name, pid, dt) VALUES ('%s', %s, '%s')"%
            (test_name, pid, test_datetime)
        )
        cur.execute("SELECT * FROM tests WHERE id = LAST_INSERT_ID()")
        latest_test = cur.fetchall()
        print(tabulate(latest_test, headers=["ID", "Test Name", "Patient ID", "Test Date and Time"], tablefmt="simple_grid"))
        confirm = input("\nDo you want to confirm adding this test? (y/n): ").strip().lower()
        if confirm == 'y':
            con.commit()
            print("\nTest added successfully!")
        else:
            con.rollback()
            print("\nTest addition cancelled.")
        add_another = input("\nDo you want to add another test? (y/n): ").strip().lower()
        if add_another != 'y':
            print("Exiting test addition process.")
            break

def add():
    while True:
        print("\nChoose an option to add:")
        print("1. Admit New Patient")
        print("2. Add New Medic")
        print("3. Add New Appointment")
        print("4. Add New Service")
        print("5. Add New Drug")
        print("6. Add New Test")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            admit_patient()
        elif choice == "2":
            add_medics()
        elif choice == "3":
            add_appointments()
        elif choice == "4":
            add_services()
        elif choice == "5":
            add_drugs()
        elif choice == "6":
            add_test()
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

def migrate_patient():
    while True:
        patient_id = input("Enter Patient ID: ").strip()
        cur.execute("SELECT * FROM patient WHERE id = %s AND doa IS NOT NULL", (patient_id,))
        patient = cur.fetchone()
        if not patient:
            print("Patient not found or patient has not been admitted.")
            continue
        old_bed_id = patient[6]
        new_bed_id = input("Enter New Bed ID: ").strip().upper()
        cur.execute("SELECT * FROM beds WHERE bid = %s", (new_bed_id,))
        new_bed = cur.fetchone()
        if not new_bed:
            print("Invalid Bed ID. Please try again.")
            continue
        if new_bed[4] == "Yes":
            print("Bed is already occupied. Please select another bed.")
            continue
        cur.execute("UPDATE patient SET bid = %s WHERE id = %s", (new_bed_id, patient_id))
        cur.execute("UPDATE beds SET occupied = 'Yes', pid = %s WHERE bid = %s", (patient_id, new_bed_id))
        cur.execute("UPDATE beds SET occupied = 'No', pid = NULL WHERE bid = %s", (old_bed_id,))
        
        if new_bed_id[0] == "O":
            while True:
                print("\nAvailable Surgeries:")
                cur.execute("SELECT * FROM cost WHERE stype = 'Surgery'")
                surgeries = cur.fetchall()
                for index, surgery in enumerate(surgeries, 1):
                    print(f"{index}. {surgery[0]}")
                surgery_choice = input("Choose Surgery: ").strip()
                if surgery_choice.isdigit() and 1 <= int(surgery_choice) <= len(surgeries):
                    surgery = surgeries[int(surgery_choice) - 1]
                    surgery_name = surgery[0]
                    break
                else:
                    print("Invalid choice. Please select a valid surgery.")

            surgery_date = date.today()
            while True:
                print("\n1. Keep Doctor Same as Consulting Doctor\n2. Enter New Doctor ID")
                doctor_choice = input("Select Option: ").strip()
                if doctor_choice == "1":
                    doctor_id = patient[11]
                    cur.execute("SELECT * FROM medics WHERE id = %s", (doctor_id,))
                    doctor = cur.fetchone()
                    doctor_name = doctor[1]
                    break
                elif doctor_choice == "2":
                    doctor_id = input("Enter Doctor ID: ").strip()
                    cur.execute("SELECT * FROM medics WHERE id = %s and dor is not null", (doctor_id,))
                    doctor = cur.fetchone()
                    if not doctor:
                        print("Invalid Doctor ID. Please try again.")
                    else:
                        doctor_name = doctor[1]
                        break
                else:
                    print("Invalid choice. Please try again.")
                    continue
            cur.execute("INSERT INTO surgery (name, date, pid, pname, did, dname) VALUES (%s, %s, %s, %s, %s, %s)",
                        (surgery_name, surgery_date, patient_id, patient[1], doctor_id, doctor_name))
        
        cur.execute("SELECT * FROM allocation WHERE pid = %s AND end IS NULL", (patient_id,))
        old_allocation = cur.fetchone()
        if old_allocation:
            cur.execute("UPDATE allocation SET end = NOW() WHERE pid = %s AND end IS NULL", (patient_id,))
        cur.execute("INSERT INTO allocation (pid, bid, start, end) VALUES (%s, %s, NOW(), NULL)", (patient_id, new_bed_id))

        cur.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
        patient_details = cur.fetchall()
        print("\nPreview of Updated Patient Details:")
        print(tabulate(patient_details, headers=["ID", "Name", "Age", "Sex", "Phone", "Address", "Bed ID", "DOA", "DOD", "Condition", "Diagnosis", "Doctor ID"], tablefmt="simple_grid"))
        
        confirm = input("\nDo you want to confirm the migration? (y/n): ").strip().lower()
        if confirm == 'y':
            con.commit()
            print("Patient successfully migrated.")
        else:
            con.rollback()
            print("Migration cancelled.")
        
        migrate_another = input("\nDo you want to migrate another patient? (y/n): ").strip().lower()
        if migrate_another != 'y':
            print("Exiting migration process.")
            break

def discharge_patient():
    while True:
        patient_id = input("Enter Patient ID: ").strip()
        cur.execute("SELECT * FROM patient WHERE id = %s AND doa IS NOT NULL", (patient_id,))
        patient = cur.fetchone()
        if not patient:
            print("Patient not found or patient has not been admitted.")
            continue
        cur.execute("UPDATE patient SET dod = CURDATE() WHERE id = %s", (patient_id,))
        bed_id = patient[6]
        cur.execute("UPDATE beds SET occupied = 'No', pid = NULL WHERE bid = %s", (bed_id,))
        cur.execute("UPDATE allocation SET end = NOW() WHERE pid = %s AND bid = %s AND end IS NULL LIMIT 1", (patient_id, bed_id))
        con.commit()
        cur.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
        patient_details = cur.fetchall()
        print("\nPatient Discharge Details:")
        print(tabulate(patient_details, headers=["ID", "Name", "Age", "Sex", "Phone", "Address", "Bed ID", "DOA", "DOD", "Condition", "Diagnosis", "Doctor ID"], tablefmt="simple_grid"))
        confirm = input("\nDo you want to confirm the discharge? (y/n): ").strip().lower()
        if confirm == 'y':
            print("Patient successfully discharged.")
            bill(patient_id)
        else:
            con.rollback()
            print("Discharge cancelled.")
        discharge_another = input("\nDo you want to discharge another patient? (y/n): ").strip().lower()
        if discharge_another != 'y':
            print("Exiting discharge process.")
            break

def bill(pid):
    cur.execute("SELECT * FROM patient WHERE id = %s", (pid,))
    patient = cur.fetchone()
    if not patient:
        print("Patient not found.")
        return
    # Initialize the bill data
    bill_data = []

    # Room charges (only for admitted patients)
    total_room_price = 0
    if patient[7]: 
        bill_data.append(["Room Charges", "",""])
        cur.execute("SELECT * FROM allocation WHERE pid = %s", (pid,))
        allocations = cur.fetchall()

        for allocation in allocations:
            bed_id = allocation[1]
            start_time = allocation[2]
            end_time = allocation[3]

            cur.execute(f"SELECT price FROM cost WHERE name LIKE '{bed_id[0]}%' AND stype = 'Room'")
            room_price = cur.fetchone()
            if end_time:
                if room_price:
                    room_price = room_price[0]
                    # Calculate stay duration in days
                    stay_duration = (end_time - start_time).total_seconds()/86400
                    price_per_bed=math.ceil(stay_duration*room_price)
                    total_room_price += price_per_bed
                    bill_data.append(["",f"{bed_id} : {start_time} - {end_time}",price_per_bed ])
        bill_data.append(["","",total_room_price])

    # Test charges (even if not admitted)
    total_test_price=0
    cur.execute("SELECT * FROM tests WHERE pid = %s", (pid,))
    tests = cur.fetchall()
    if len(tests)!=0:
        bill_data.append(["Test Charges","",""])
        for test in tests:
            cur.execute("SELECT price FROM cost WHERE name = %s AND stype = 'Test'", (test[1],))
            test_price = cur.fetchone()
            if test_price:
                test_price = test_price[0]
                total_test_price+=test_price
                bill_data.append(["", f"{test[1]} : {test[3]}", test_price])
        bill_data.append(["","",total_test_price])

    # Surgery charges (only for admitted patients)
    total_surgery_price=0
    if patient[7]:
        cur.execute("SELECT * FROM surgery WHERE pid = %s", (pid,))
        surgeries = cur.fetchall()
        if len(surgeries)!=0:
            
            bill_data.append(["Surgery Cost","",""])
            for surgery in surgeries:
                cur.execute("SELECT price FROM cost WHERE name = %s AND stype = 'Surgery'", (surgery[0],))
                surgery_price = cur.fetchone()
                if surgery_price:
                    surgery_price = surgery_price[0]
                    total_surgery_price+=surgery_price
                    bill_data.append(["", f"{surgery[0]} : {surgery[5]} : {surgery[1]}", surgery_price])

    # Appointments charges
    total_appointment_fee=0
    cur.execute("SELECT * FROM appointments WHERE pid = %s", (pid,))
    appointments = cur.fetchall()
    if len(appointments)!=0:
        
        bill_data.append(["Doctor Consultation","",""])
        for appointment in appointments:
            cur.execute("SELECT fee FROM medics WHERE id = %s", (appointment[1],))
            doctor_fee = cur.fetchone()
            if doctor_fee:
                doctor_fee = doctor_fee[0]
                total_appointment_fee+=doctor_fee
                bill_data.append(["", f"{appointment[2]} : {appointment[3]}", doctor_fee])
        bill_data.append(["","",total_appointment_fee])

    # Miscellaneous charges
    total_misc_price = 0
    if patient[7]:
        cur.execute("SELECT * FROM cost WHERE stype = 'Misc'", ())
        misc_services = cur.fetchall()
        if len(misc_services)!=0:
            bill_data.append(["Miscellaneous","",""])

            for misc in misc_services:
                misc_price = misc[2]
                total_misc_price += misc_price
                bill_data.append(["", f"{misc[0]}", misc_price])
            bill_data.append(["","",total_misc_price])

    # Prescribed drugs charges
    total_drugs_price = 0
    ch=input("Has the doctor prescribed any drugs? (Y/N)? : ").strip().lower()
    if ch=='y':
        bill_data.append(["Prescribed Drugs","",""])
        
        while True:
            drug_id = int(input("Enter drug ID (or 0 to stop): "))
            if drug_id == 0:
                break
            cur.execute("SELECT * FROM drugs WHERE id = %s", (drug_id,))
            drug = cur.fetchone()
            if drug:
                dosage = int(input(f"Enter dosage for {drug[1]}: "))
                drug_price = drug[2] * dosage
                total_drugs_price+=drug_price
                cur.execute(f"update drugs set stock=stock-{dosage} where id={drug_id}")
                bill_data.append(["", f"{drug[1]} * {dosage}", drug_price])
        
            else:
                print("Drug ID not found. Please try again.")
        bill_data.append(["","",total_drugs_price])

    # Add GST (5%)
    total_price = total_appointment_fee+total_drugs_price+total_misc_price+total_test_price+total_room_price+total_surgery_price
    gst = total_price * 0.05
    bill_data.append(["GST","5%",gst])

    # Ask for discount
    discount_percent = float(input("Enter discount percentage: "))
    discount = total_price * (discount_percent / 100)
    bill_data.append(["Discounts",f"{discount_percent}%",discount])

    # Total
    net_total = total_price + gst - discount
    bill_data.append(["", "", net_total])

    cur.execute("""
            INSERT INTO bill (pid, pname, date, rent, consfee, test, drugs, misc, surgery, tax, disc, net)
            VALUES (%s, %s, CURDATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (pid, patient[1], total_room_price, total_appointment_fee, total_test_price, total_drugs_price, total_misc_price, total_surgery_price, gst, discount, net_total))
    cur.execute("select last_insert_id()")
    bill_id=cur.fetchone()[0]
    print()
    print("="*90,"HOSPITAL BILL","="*90,"\n")
    print("\t\tBILL ID :",bill_id, "\t\t BILLING DATE :",date.today(), "\n")
    print("-"*90,"Patient Details","-"*90,"\n")
    print(f"Patient ID : {pid} \t\t\t\t Patient Name: {patient[1]} \nAge: {patient[2]} \t\t\t\t\t Sex: {patient[3]}")
    print(f"Phone: {patient[4]} \t\t\t\t Address: {patient[5]} \nDiagnosis: {patient[10]}")
    print(f"Admission Date: {patient[7]} \t\t\t Discharge Date: {patient[8]}\n")

    # Print the bill using tabulate
    headers = ["Breakup", "Narration", "Price"]
    print(tabulate(bill_data, headers=headers, tablefmt="fancy_grid"))

    # Ask for confirmation to insert into the bill table
    confirm = input("Do you want to confirm the bill? (y/n): ").strip().lower()
    if confirm == 'y':
        # Insert the data into the bill table
        con.commit()
        print("Bill confirmed and saved.")

def update_appointments():
    while True:
        appointment_id = input("Enter the appointment ID to update: ").strip()
        if appointment_id.isdigit():
            appointment_id = int(appointment_id)
            cur.execute("SELECT * FROM appointments WHERE id = %s", (appointment_id,))
            data = cur.fetchall()
            if data:
                break
            else:
                print(f"Appointment with ID {appointment_id} not found.")
        else:
            print("Invalid input. Please enter a valid appointment ID.")
    
    while True:
        print("\nChoose the new status:")
        print("1. Completed")
        print("2. Cancelled")
        status_choice = input("Enter 1 for Completed or 2 for Cancelled: ").strip()
        if status_choice == "1":
            new_status = "Completed"
            break
        elif status_choice == "2":
            new_status = "Cancelled"
            break
        else:
            print("Invalid choice. Please enter 1 for Completed or 2 for Cancelled.")

    cur.execute("UPDATE appointments SET status = %s WHERE id = %s", (new_status, appointment_id))
    print("Confirmation Preview: ")
    headers = ["ID", "Doctor", "Patient", "Date", "Start Time", "End Time", "Status"]
    print(tabulate(data, headers=headers, tablefmt="simple_grid"))
    confirmation = input("Do you want to proceed? (y/n): ").strip().lower()
    
    if confirmation == 'y':
        doctor_id = data[0][1]  # doctor ID from the appointment data
        appt_date = data[0][3]  # appointment date
        start_time = data[0][4]  # start time
        end_time = data[0][5]  # end time
        appt_entry = f"{appt_date}, {start_time} - {end_time}\n"
        cur.execute("SELECT appts FROM medics WHERE id = %s", (doctor_id,))
        doctor_appts = cur.fetchone()[0]
        
        if doctor_appts:
            updated_appts = doctor_appts.replace(appt_entry, "")
            cur.execute("UPDATE medics SET appts = %s WHERE id = %s", (updated_appts, doctor_id))
        
        con.commit()
        print(f"Appointment {appointment_id} status has been updated to {new_status}.")
    else:
        con.rollback()
        print("Appointment status update cancelled.")

def update_working_hours():
    # Fetch current working hours
    doctor_id=int(input("Enter ID of the doctor whose working hours are to be updated: "))
    cur.execute("SELECT work FROM medics WHERE id = %s", (doctor_id,))
    result = cur.fetchone()

    if not result:
        print("Doctor ID not found.")
        return

    work_hours = result[0]
    print(f"\nCurrent working hours:\n{work_hours}")
    print("\nEnter Working Hours (leave blank if holiday):")
    work_hours = []
    days=["Monday","Tuesday","Wednesday","Thurday","Friday","Saturday","Sunday"]
    for day in days:
        while True:
            start_time = input(f"Enter New Start Time for {day} (HH:MM, leave blank if holiday): ").strip()
            end_time = input(f"Enter New End Time for {day} (HH:MM, leave blank if holiday): ").strip()
            if not start_time and not end_time:  # Holiday
                break
            if start_time and end_time:  # Both times provided
                try:
                    start_dt = datetime.strptime(start_time, "%H:%M")
                    end_dt = datetime.strptime(end_time, "%H:%M")
                    if end_dt > start_dt:
                        work_hours.append(f"{day[:3]}, {start_time}-{end_time}")
                        break
                    else:
                        print("End time must be later than start time. Please re-enter.")
                except ValueError:
                    print("Invalid time format. Please enter in HH:MM format.")
            else:
                print("Both start and end time must be provided or leave both blank for a holiday.")
    updated_work_hours = "\n".join(work_hours)
    cur.execute("UPDATE medics SET work = %s WHERE id = %s", (updated_work_hours, doctor_id))
    cur.execute("select* from medics where id="+ str(doctor_id))
    data=cur.fetchall()
    # Confirm changes
    header=["Doctor_ID", "Name", "Specialization", "Phone","Fee","Working Hours","Appointments","Join_Date","Resig_Date"]
    print("\nUpdated working hours preview:")
    print(tabulate(data,headers=header,tablefmt="simple_grid"))
    confirm = input("Do you want to commit these changes? (yes/no): ").strip().lower()
    if confirm == "yes":
        con.commit()  
        print("Working hours updated successfully.")
    else:
        con.rollback()
        print("Changes discarded.")

def update_stock():
    headers = ["ID", "Name", "Price", "Manufacturer", "Stock", "Short Composition 1", "Short Composition 2"] 
    while True:
        while True:
            drug_id = input("Enter the drug ID to update stock: ").strip()
            if drug_id.isdigit():
                drug_id = int(drug_id)
                cur.execute("SELECT * FROM drugs WHERE id = %s", (drug_id,))
                drug_data = cur.fetchall()
                if drug_data:
                    print(f"\nDrug Details:")
                    print(tabulate(drug_data, headers=headers, tablefmt="simple_grid"))
                    break
                else:
                    print(f"No drug found with ID {drug_id}. Please try again.")
            else:
                print("Invalid input. Please enter a valid numeric drug ID.")

        while True:
            additional_stock = input("Enter the amount of stock to add: ").strip()
            if additional_stock.isdigit():
                additional_stock = int(additional_stock)
                if additional_stock > 0:
                    break
                else:
                    print("Stock amount must be greater than 0. Please try again.")
            else:
                print("Invalid input. Please enter a valid numeric stock amount.")

        cur.execute("UPDATE drugs SET stock = stock + %s WHERE id = %s", (additional_stock, drug_id))
        cur.execute("SELECT * FROM drugs WHERE id = %s", (drug_id,))
        updated_data = cur.fetchall()
        print(f"\nUpdated Drug Details:")
        print(tabulate(updated_data, headers=headers, tablefmt="simple_grid"))
        
        confirmation = input("Do you want to confirm this update? (y/n): ").strip().lower()
        if confirmation == 'y':
            con.commit()
            print(f"Stock for drug ID {drug_id} successfully updated. {additional_stock} units added.")
        else:
            con.rollback()
            print("Stock update cancelled.")

        another = input("Do you want to add stock for another drug? (y/n): ").strip().lower()
        if another != 'y':
            print("Exiting stock update.")
            break

def update_service_cost():
    headers = ["S.No", "Service Name", "Service Type", "Current Price"]
    cur.execute("SELECT name, stype, price FROM cost")
    services = cur.fetchall()
    
    # Add serial numbers to the services
    services_with_serial = [(i + 1, *service) for i, service in enumerate(services)]
    print("\nAvailable Services:")
    print(tabulate(services_with_serial, headers=headers, tablefmt="simple_grid"))
    
    while True:
        try:
            selected_no = int(input("Enter the serial number of the service to update: ").strip())
            if 1 <= selected_no <= len(services_with_serial):
                selected_service = services_with_serial[selected_no - 1]
                break
            else:
                print(f"Invalid serial number. Please choose a number between 1 and {len(services_with_serial)}.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric serial number.")

    print(f"\nYou selected: {selected_service[1]} ({selected_service[2]}) with current price {selected_service[3]}")

    while True:
        try:
            new_price = int(input("Enter the new price for the service: ").strip())
            if new_price > 0:
                break
            else:
                print("Price must be a positive value. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric price.")

    cur.execute("UPDATE cost SET price = %s WHERE name = %s AND stype = %s", (new_price, selected_service[1], selected_service[2]))

    cur.execute("SELECT name, stype, price FROM cost WHERE name = %s AND stype = %s", (selected_service[1], selected_service[2]))
    updated_service = cur.fetchall()

    print("\nUpdated Service Details:")
    print(tabulate(updated_service, headers=headers[1:], tablefmt="simple_grid"))
    confirmation = input("Do you want to confirm this update? (y/n): ").strip().lower()
    if confirmation == 'y':
        con.commit()
        print(f"The cost for {selected_service[1]} ({selected_service[2]}) has been updated to {new_price}.")
    else:
        con.rollback()
        print("Service cost update cancelled.")

def update_drug_price():
    while True:
        headers = ["ID", "Name", "Price", "Manufacturer", "Stock", "Short Composition 1", "Short Composition 2"]
        while True:
            drug_id = input("\nEnter the drug ID to update price: ").strip()
            if drug_id.isdigit():
                drug_id = int(drug_id)
                cur.execute("SELECT * FROM drugs WHERE id = %s", (drug_id,))
                drug_data = cur.fetchone()
                if drug_data:
                    print("\nSelected Drug Details:")
                    print(tabulate([drug_data], headers=headers, tablefmt="simple_grid"))
                    break
                else:
                    print(f"No drug found with ID {drug_id}. Please try again.")
            else:
                print("Invalid input. Please enter a valid numeric drug ID.")

        while True:
            try:
                new_price = float(input("Enter the new price for the drug: ").strip())
                if new_price > 0:
                    break
                else:
                    print("Price must be a positive value. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric price.")


        cur.execute("UPDATE drugs SET price = %s WHERE id = %s", (new_price, drug_id))
        cur.execute("SELECT * FROM drugs WHERE id = %s", (drug_id,))
        updated_drug = cur.fetchone()

        print("\nUpdated Drug Details:")
        print(tabulate([updated_drug], headers=headers, tablefmt="simple_grid"))

        confirmation = input("Do you want to confirm this update? (y/n): ").strip().lower()
        if confirmation == 'y':
            con.commit()
            print(f"Drug price updated successfully to {new_price} for ID {drug_id}.")
        else:
            con.rollback()
            print("Price update cancelled.")

        ch=input("Do You Want to Update More (Y/N)? : ").strip.upper()
        if ch!="Y":
            break

def retire_medic():
    headers = ["ID", "Name", "Specialization", "Phone", "Fee", "Work Schedule", "Appointments", "Date of Joining", "Date of Retirement"]
    view_medics()
    while True:
        medic_id = input("\nEnter the medic ID to retire: ").strip()
        if medic_id.isdigit():
            medic_id = int(medic_id)
            cur.execute("SELECT * FROM medics WHERE id = %s AND dor IS NULL", (medic_id,))
            medic_data = cur.fetchone()
            if medic_data:
                print("\nSelected Medic Details:")
                print(tabulate([medic_data], headers=headers, tablefmt="simple_grid"))
                break
            else:
                print(f"No active medic found with ID {medic_id}. Please try again.")
        else:
            print("Invalid input. Please enter a valid numeric medic ID.")
    confirmation = input("Do you want to retire this medic? (y/n): ").strip().lower()
    if confirmation == 'y':
        cur.execute("UPDATE medics SET dor = CURDATE(), appts=NULL WHERE id = %s", (medic_id,))
        cur.execute("update appointments set status='Cancelled' where status='Scheduled' and did="+str(medic_id))
        con.commit()
        print(f"Medic with ID {medic_id} has been retired successfully.")
    else:
        con.rollback()
        print("Retirement process cancelled.")

def update():
    while True:
        print("\n1. Migrate Patient")
        print("2. Update Appointments")
        print("3. Update Doctor Working Hours")
        print("4. Update Drug Stock(s)")
        print("5.  Update Drug Price(s)")
        print("6. Update Service Charges")
        print("7. Retire Medic\n")

        ch=int(input("Enter Your Choice (1-7)").strip())
        if ch==1:
            migrate_patient()
            break
        elif ch==2:
            update_appointments()
            break
        elif ch==3:
            update_working_hours()
            break
        elif ch==4:
            update_stock()
            break
        elif ch==5:
            update_drug_price()
            break
        elif ch==6:
            update_service_cost()
            break
        elif ch==7:
            retire_medic()
            break

def menu():
    k=True
    while k:
        print()
        print("\t"*8,"MAIN MENU", "\t"*8)
        print()
        print("\t\t\t\t [1] View   \t\t [2] Search    \t\t [3] Add\n")
        print("\t\t\t\t [4] Update \t\t [5] Discharge \t\t [6] Generate Bill\n")
        print("\t\t\t\t [7] Exit\n")
        ch=int(input("Enter Your Choice: ").strip())
        k=False
        if ch==1:
            view()
        elif ch==2:
            search()
        elif ch==3:
            add()
        elif ch==4:
            update()
        elif ch==5:
            discharge_patient()
        elif ch==6:
            pid=int(input("Enter Patient ID whose bill is to be generated: ").strip())
            bill(pid)
        elif ch==7:
            terminate()
        else:
            print("Invalid choice.")
            k=True
            continue
        loop()

def terminate():
    con.close()
    sys.exit()


def loop():
    menu()

menu()       
