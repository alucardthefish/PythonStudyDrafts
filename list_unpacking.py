"""Unpacking list using * character: only one unpacking is allowed per list"""

employee_info = [
    "John",
    "Duncan",
    "1998-03-23",
    "5 feet 9 inches",
    "68 Kg",
    "$6.700,00",
    "Company Car",
    "Spotify membership",
    "Internet bonus",
    "Meals bonus",
]

name, last_name, dob, height, weight, salary, *perks = employee_info
print("----------------------First-Unpacking-list---------------------------")
print("name: ", name)
print("last_name: ", last_name)
print("date of birth: ", dob)
print("height: ", height)
print("weight: ", weight)
print("salary: ", salary)
print("perks: ", perks)

print("----------------------Second-Unpacking-list---------------------------")
(
    employee_name,
    employee_last_name,
    *personal_employee_info,
    employee_salary,
    perk1,
    perk2,
    perk3,
    perk4,
) = employee_info
print("employee_name :", employee_name)
print("employee_last_name :", employee_last_name)
print("personal_employee_info :", personal_employee_info)
print("employee_salary :", employee_salary)
print("perk 1 :", perk1)
print("perk 2 :", perk2)
print("perk 3 :", perk3)
print("perk 4 :", perk4)
