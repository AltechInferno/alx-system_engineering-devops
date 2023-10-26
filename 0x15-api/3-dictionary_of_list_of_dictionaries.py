#!/usr/bin/python3
import json
import requests
import sys

def get_user_tasks(user_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, user_id)
    tasks_url = "{}/todos?userId={}".format(base_url, user_id)

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    if user_response.status_code == 404 or tasks_response.status_code == 404:
        return None, None

    user_data = user_response.json()
    tasks_data = tasks_response.json()
    
    return user_data, tasks_data

def export_all_tasks_to_json():
    all_tasks = {}

    for user_id in range(1, 11):
        user_data, tasks_data = get_user_tasks(user_id)
        if user_data and tasks_data:
            user_id_str = str(user_id)
            username = user_data["username"]

            user_tasks = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in tasks_data]

            all_tasks[user_id_str] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)

if __name__ == "__main__":
    export_all_tasks_to_json()

