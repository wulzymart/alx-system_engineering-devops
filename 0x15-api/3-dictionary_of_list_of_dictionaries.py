#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"

    users = requests.get(base_url).json()

    users_js = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = f'{base_url}/{user_id}/todos/'
        tasks = requests.get(url).json()
        users_js[user_id] = []
        for task in tasks:
            users_js[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_js, file)
