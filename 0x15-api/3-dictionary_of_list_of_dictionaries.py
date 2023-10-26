#!/usr/bin/python3
"""JSONPlaceholder API to get information about employee and exports"""
import json
import requests
import sys


if __name__ == "__main__":

    apiUrl = 'https://jsonplaceholder.typicode.com/'
    userData = '{}users'.format(apiUrl)
    res = requests.get(userData)
    obj = res.json()
    dic0_task = {}
    for userData in obj:
        username = userData.get('username')
        userId = userData.get('id')
        todos = '{}todos?userId={}'.format(apiUrl, userId)
        res = requests.get(todos)
        tasks = res.json()
        all_task = []
        for task in tasks:
            dic_task = {"username": username,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            all_task.append(dic_task)

        dic_task[str(userId)] = all_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(dic_task, f)
