#!/usr/bin/python3
'''Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
'''

import requests
import sys


def main(args):
    '''function that returns information using REST API
    '''

    if len(args) > 1:
        usr = args[1]
        url = "https://jsonplaceholder.typicode.com"
        req = requests.get("{}/users/{}".format(url, usr))
        name = req.json().get("name")

        if name is not None:
            req = requests.get("{}/todos?userId={}".format(url, usr))
            request = req.json()

            tasks = len(request)
            completed = []

            for task in request:
                if task.get("completed") is True:
                    completed.append(task)
            i = len(completed)
            print("Employee {} is done with tasks({}/{}):".format(name, i,
                                                                  tasks))
            for title in completed:
                print("\t {}".format(title.get("title")))


if __name__ == "__main__":
    main(sys.argv)
