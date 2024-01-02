#!/usr/bin/python3
'''python script to export data in the CSV format
'''

import csv
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    usr = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(id), 'w', newline='') as file:
        tasks = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            tasks.writerow([int(id), usr.get("username"),
                           task.get("completed"), task.get("title")])
