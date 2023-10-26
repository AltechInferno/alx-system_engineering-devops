#!/usr/bin/python3
"""JSONPlaceholder API to get information about employee and exports """
import json
import requests
import sys


if __name__ == "__main__":

    apiUrl = 'https://jsonplaceholder.typicode.com/'
    userId = sys.argv[1]
    userData = '{}users/{}'.format(apiUrl, userId)
    res = requests.get(userData)
    obj = res.json()
    username = obj.get('username')

    todos = '{}todos?userId={}'.format(apiUrl, userId)
    res = requests.get(todos)
    tasks = res.json()
    all_task = []
    for task in tasks:
        dic_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        all_task.append(dic_task)

    dic0_task = {str(userId): all_task}
    filename = '{}.json'.format(userId)
    with open(filename, mode='w') as f:
        json.dump(dic0_task, f)
