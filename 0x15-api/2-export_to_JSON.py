#!/usr/bin/python3
"""REST API for employees"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    requested_employee_id = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f'{baseUrl}/{requested_employee_id}'

    employee = requests.get(url).json()
    employee_name = employee.get('username')

    todoUrl = f"{url}/todos"
    tasks = requests.get(todoUrl).json()

    employee_js = {requested_employee_id: []}
    for task in tasks:
        employee_js[requested_employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })
    with open('{}.json'.format(requested_employee_id), 'w') as file:
        json.dump(employee_js, file)
