import csv

with open('companies.csv', 'w') as csvfile:
    x = ['name', 'type', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=x)
    writer.writeheader()
    writer.writerow({'name': 'Codecademy', 'type': 'Learning', 'age': '6'})
    writer.writerow({'age': '3'})
    writer.writerow({'name': 'Google', 'type': 'Search'})

"""
After running the above code, companies.csv will contain the following information:

name,type
Codecademy,Learning
Google,Search
"""
