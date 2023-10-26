#!/usr/bin/python3
""" uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":

    apiUrl = 'https://jsonplaceholder.typicode.com/'
    input = sys.argv[1]
    userData = '{}users/{}'.format(apiUrl, input)
    res = requests.get(userData)
    obj = res.json()
    print("Employee {} is done with tasks".format(obj.get('name')), end="")

    todos = '{}todos?userId={}'.format(apiUrl, input)
    res = requests.get(todos)
    tasks = res.json()
    all_task = []
    for task in tasks:
        if task.get('completed') is True:
            all_task.append(task)

    print("({}/{}):".format(len(all_task), len(tasks)))
    for task in all_task:
        print("\t {}".format(task.get("title")))
