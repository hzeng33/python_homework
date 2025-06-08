# Task 3: List Comprehensions Practice

import pandas as pd

df = pd.read_csv("../csv/employees.csv")

full_names = [f"{row["first_name"]}  {row["last_name"]}" for index, row in df.iterrows()]
print("Employees list\n", full_names)

names_with_e = [name for name in full_names if "e" in name.lower()]
print("Employees' names have e\n", names_with_e)