#!/usr/bin/python3
""" JSONPlaceholder API to get information about employee and export"""
import csv
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
        all_task.append([userId,
                       username,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(userId)
    with open(filename, mode='w') as employee_file:
        employee_export = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in all_task:
            employee_export.writerow(task)
