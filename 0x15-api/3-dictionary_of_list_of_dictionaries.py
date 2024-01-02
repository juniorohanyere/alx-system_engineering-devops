#!/usr/bin/python3
'''python script to export data in the JSON format
'''

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    dic = requests.get(url, verify=False).json()
    a = {}
    b = {}

    for usr in dic:
        id = usr.get("id")
        a[id] = []
        b[id] = usr.get("username")

    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [a.get(task.get("userId")).append({"task": task.get("title"),
                                       "completed": task.get("completed"),
                                       "username": b.get(task.get("userId"))})

     for task in todo]

    with open("todo_all_employees.json", "w") as file:
        json.dump(a, file)
