# Employee 1
employee_object1 = {
    "ID": 1,
    "Name": "John Doe",
    "Department": "Sales",
    "Age": 30,
    "Email": "john.doe@company.com"
}

# Employee 2
employee_object2 = {
    "ID": 2,
    "Name": "Jane Smith",
    "Department": "Human Resources",
    "Age": 25,
    "Email": "jane.smith@company.com"
}

# Employee 3
employee_object3 = {
    "ID": 3,
    "Name": "Mark Johnson",
    "Department": "IT",
    "Age": 40,
    "Email": "mark.johnson@company.com"
}

# Employee 4
employee_object4 = {
    "ID": 4,
    "Name": "Lisa Wong",
    "Department": "Marketing",
    "Age": 28,
    "Email": "lisa.wong@company.com"
}

# Employee 5
employee_object5 = {
    "ID": 5,
    "Name": "Paul McDonald",
    "Department": "Finance",
    "Age": 35,
    "Email": "paul.mcdonald@company.com"
}

# List of Employees
employees = [employee_object1, employee_object2, employee_object3, employee_object4, employee_object5]

# Iterate through the list of employees and print details
for employee in employees:
    print(f"ID: {employee['ID']}, Name: {employee['Name']}, Department: {employee['Department']}, "
          f"Age: {employee['Age']}, Email: {employee['Email']}")
