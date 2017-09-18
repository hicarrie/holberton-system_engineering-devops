#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress
"""

import sys
import requests
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    filename = sys.argv[1] + ".csv"

    employee = requests.get(url + "users/" + employee_id)
    employee = employee.json()

    tasks = requests.get(url + "todos?userId=" + employee_id)
    tasks = tasks.json()

    with open(filename, mode="w") as a_file:
        for item in tasks:
            print('"{}", "{}", "{}", "{}"'.format(item.get('userId'),
                                                  employee.get('username'),
                                                  item.get('completed'),
                                                  item.get('title')))
