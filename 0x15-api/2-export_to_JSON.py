#!/usr/bin/python3
import requests
import sys
import json

def get_employee_info(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get user information
    user_response = requests.get('{}users/{}'.format(base_url, employee_id))
    user_data = user_response.json()

    # Get user's TODO list
    todos_response = requests.get('{}todos?userId={}'.format(base_url, employee_id))
    todos_data = todos_response.json()

    return user_data, todos_data

def export_to_json(employee_id, user_data, todos_data):
    json_data = {str(employee_id): []}
    for task in todos_data:
        json_data[str(employee_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    json_file = '{}.json'.format(employee_id)
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    print("Data exported to {}.json".format(employee_id))

def main():
    if len(sys.argv) != 2:
        print("Usage: python export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todos_data = get_employee_info(employee_id)

    export_to_json(employee_id, user_data, todos_data)

if __name__ == "__main__":
    main()
