# Task 2: Read a CSV File
import csv

def read_employees():
    employee_list = []
    employee_dict = {}
    
    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            data = csv.reader(file)
            for i, row in enumerate(data):
                if i == 0:
                    employee_dict["fields"] = row
                else:
                    employee_list.append(row)
            employee_dict["rows"] = employee_list
    except Exception as e:
        print(f"Error reading file: {e}")
        
    file.close
    return employee_dict

employees = read_employees()
# print(employees)


# Task 3: Find the Column Index
def column_index(column_name): 
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
# print(employee_id_column)


# Task 4: Find the Employee First Name
def first_name(row_num):
    first_name_column_index = column_index("first_name")
    return employees["rows"][row_num][first_name_column_index]


# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches  


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key = lambda row : row[column_index("last_name")])
    return employees["rows"]

# print(sort_by_last_name())


# Task 8: Create a dict for an Employee
def employee_dict(row):
    key_list = []
    value_list = []
    for i, key_item in enumerate(employees["fields"]):
        if i > 0:
            key_list.append(key_item)
    for i, row_item in enumerate(row):
        if i > 0:
            value_list.append(row_item)
    result = dict(zip(key_list, value_list))
    return result

# print(employee_dict(employees["rows"][1]))


# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    emp_id_index = column_index("employee_id")
    result = {}
    for row in employees["rows"]:
        emp_id = row[emp_id_index]
        emp_dict = employee_dict(row)
        result[emp_id] = emp_dict
    return result


# Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")


# Task 11: Creating Your Own Module
import custom_module

def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret("fLyinGyAy")
# print(custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv
def  read_minutes():
    minutes1 = {} 
    minutes2 = {}
    minutes1_list = []
    minutes2_list = []
    
    try:
        with open("../csv/minutes1.csv", "r", newline="") as file:
            data = csv.reader(file)
            for i, row in enumerate(data):
                if i == 0:
                    minutes1["fields"] = row
                else:
                    minutes1_list.append(tuple(row))
            minutes1["rows"] = tuple(minutes1_list)
        
        with open("../csv/minutes2.csv", "r", newline="") as file:
            data = csv.reader(file)
            for i, row in enumerate(data):
                if i == 0:
                    minutes2["fields"] = row
                else:
                    minutes2_list.append(tuple(row))
            minutes2["rows"] = tuple(minutes2_list)
      
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
# print(minutes1)
# print(minutes2)


# Task 13: Create minutes_set
def create_minutes_set():
    result_set = set(minutes1["rows"]).union(set(minutes2["rows"]))
    return result_set

minutes_set = create_minutes_set()
#print(minutes_set)


# Task 14: Convert to datetime
from datetime import datetime

def  create_minutes_list():
    minutes_list = list(minutes_set)
    result_list = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    return list(result_list)

minutes_list = create_minutes_list()


# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    new_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    
    try:
        with open("./minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            for row in new_list:
                writer.writerow(row)
    except Exception as e:
        print(f"Error writing file: {e}")
    
    return new_list

sorted_list = write_sorted_list()
# print(sorted_list)