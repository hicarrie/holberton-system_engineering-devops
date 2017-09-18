#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress
"""

import sys
import requests
import json


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
            task_dict['task'] = item['title']
            task_dict['completed'] = item['completed']
            task_dict['username'] = employee['username']
            tasks_list.append(task_dict)

        employee_tasks[employee_id] = tasks_list

    with open(filename, mode="w") as json_file:
        json.dump(employee_tasks, json_file)
