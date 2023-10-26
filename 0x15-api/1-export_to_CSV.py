#!/usr/bin/python3
import requests
import sys
import csv

def get_employee_info(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get user information
    user_response = requests.get('{}users/{}'.format(base_url, employee_id))
    user_data = user_response.json()

    # Get user's TODO list
    todos_response = requests.get('{}todos?userId={}'.format(base_url, employee_id))
    todos_data = todos_response.json()

    return user_data, todos_data

def export_to_csv(employee_id, user_data, todos_data):
    csv_file = '{}.csv'.format(employee_id)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for task in todos_data:
            writer.writerow([employee_id, user_data['username'], task['completed'], task['title']])

def main():
    if len(sys.argv) != 2:
        print("Usage: python export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todos_data = get_employee_info(employee_id)

    export_to_csv(employee_id, user_data, todos_data)
    print("Data exported to {}.csv".format(employee_id))

if __name__ == "__main__":
    main()

