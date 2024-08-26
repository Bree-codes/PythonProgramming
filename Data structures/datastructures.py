"""#Lists data structures
from os import popen

students1 = ["Steve", "Bree", "Bob", "Chebby", "Levi"]
students1.append("Kev")
students1.remove("Bob")
var = students1[0]
print(var)
print(students1)


#Tuples
family = ("Mother","Father","Sister","Brother")
var = family[0]
print(family)

#Dictionaries
people = {
    "Name": "Bree",
    "Age": 20,
    "Gender": "Female"
}
print(people)"""

#List of dictionaries
students = [
    {
    "Name": "Bree",
    "Age": 20,
    "Gender": "Female"
    },
    {
    "Name": "Breshy",
    "Age": 20,
    "Gender": "Female"
    }
]
print(students[0])
print(students[0] ["Name"])