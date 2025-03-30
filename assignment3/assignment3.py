import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

data_dict = {
    "Name":["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data_dict)
# print(df)
task1_data_frame = df

task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
# print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"].add(1)
# print(task1_older)

task1_older.to_csv("employees.csv", index=False)


# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv("employees.csv")
# print(task2_employees)

json_employees = pd.read_json("additional_employees.json")
# print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
# print(more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = more_employees.head(3)
# print(first_three)
last_two = more_employees.tail(2)
# print(last_two) 
employee_shape = more_employees.shape
# print(employee_shape)

# print(more_employees.info())


# Task 4: Data Cleaning
# 1.Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv("dirty_data.csv")
# print(dirty_data)
clean_data = dirty_data.copy()

# 2.Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
# print(clean_data)

# 3.Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce").ffill().astype(int)
# print(clean_data)

# 4.Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
import numpy as np
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"], errors="coerce").replace({"unknown" : np.nan, "n/a": np.nan})
# print(clean_data)

# 5.Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data["Age"].mean()
median_salary = clean_data["Salary"].median()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
# print(clean_data)

# 6.Convert Hire Date to datetime
clean_data["Hire Date"] = clean_data["Hire Date"].str.strip()
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format="mixed")
# print(clean_data)

# 7.Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)