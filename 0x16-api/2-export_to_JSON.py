#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress
"""

import sys
import requests
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    filename = employee_id + ".json"

    employee = requests.get(url + "users/" + employee_id)
    employee_json = employee.json()

    tasks = requests.get(url + "todos?userId=" + employee_id)
    tasks_json = tasks.json()

    tasks_list = []
    for item in tasks_json:
        tasks_list.append(item)

    employee_tasks = {}
    employee_tasks[employee_id] = tasks_list

    with open(filename, mode="w") as json_file:
        json.dump(employee_tasks, json_file)
