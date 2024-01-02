#!/usr/bin/python3
'''python script to export data in the JSON format
'''

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    usr = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?usrId={}".format(id)
    todo = requests.get(url, verify=False).json()
    name = usr.get("username")
    tasks = [{"task": tasks.get("title"), "username": name,
             "completed": tasks.get("completed")} for tasks in todo]
    task = {}
    task[id] = tasks

    with open("{}.json".format(id), "w") as file:
        json.dump(task, file)
