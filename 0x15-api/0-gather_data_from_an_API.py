#!/usr/bin/python3
"""Rest API for employees"""

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
    tasks_done = []

    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)

    print(f"Employee {employee_name} \
is done with tasks({len(tasks_done)}/{len(tasks)}):")

    for task in tasks_done:
        print(f"\t {task.get('title')}")
