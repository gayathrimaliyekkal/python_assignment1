import json

employee_name = ["Aashrith","Badri","Gayathri","Kiran","Omesh","Rakesh","Sabari","Vamsi"]
emp = open('employee_details.txt','w')                                                  #storing into a text file
emp.write(json.dumps(employee_name))
emp.close()