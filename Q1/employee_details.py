employee_name = ["Aashrith","Badri","Gayathri","Kiran","Omesh","Rakesh","Sabari","Vamsi"]
for emp in employee_name:
    print(emp)
employee_name.extend(["Balu","Hari"])              #adding new names to the list
print(employee_name)
employee_name.remove("Balu")                       #removing a name
print(employee_name)

