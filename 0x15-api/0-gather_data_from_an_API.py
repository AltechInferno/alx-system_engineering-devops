#!/usr/bin/python3
import requests
import sys

def get_employee_info(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get user information
    user_response = requests.get('{}users/{}'.format(base_url, employee_id))
    user_data = user_response.json()

    # Get user's TODO list
    todos_response = requests.get('{}todos?userId={}'.format(base_url, employee_id))
    todos_data = todos_response.json()

    return user_data, todos_data

def main():
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todos_data = get_employee_info(employee_id)

    user_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(user_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))

if __name__ == "__main__":
    main()

