#!/usr/bin/python3
"""
Returns information about all employees' TODO list progress in JSON format
"""

import requests
import json
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    filename = "todo_all_employees.json"

    employees = requests.get(url + "users/")
    employees = employees.json()

    employee_tasks = {}
    for employee in employees:
        employee_id = employee['id']
        tasks = requests.get(url + "todos?userId=" + str(employee_id))
        tasks = tasks.json()

        tasks_list = []
        for item in tasks:
            task_dict = {}
            task_dict.get('task') = item.get('title')
            task_dict.get('completed') = item.get('completed')
            task_dict.get('username') = employee.get('username')
            tasks_list.append(task_dict)

        employee_tasks[employee_id] = tasks_list

    with open(filename, mode="w") as json_file:
        json.dump(employee_tasks, json_file)
