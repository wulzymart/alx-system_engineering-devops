#!/usr/bin/python3
"""REST API for employees"""

import requests
from sys import argv


if __name__ == '__main__':
    requested_employee_id = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f'{baseUrl}/{requested_employee_id}'

    employee = requests.get(url).json()
    employee_name = employee.get('name')

    todoUrl = f"{url}/todos"
    tasks = requests.get(todoUrl).json()

    with open(f'{requested_employee_id}.csv', 'w') as file:
        for task in tasks:
            file.write(f'"{requested_employee_id}","{employee_name}",\
"{task.get("completed")}","{task.get("title")}"\n')
