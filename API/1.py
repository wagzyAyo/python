#!/usr/bin/python3
"""This module request data from 
jsonplaceholder"""
import requests
import sys


if __name__ == '__main__':
    end_point = "https://jsonplaceholder.typicode.com/"
    id=1
    response = requests.get(f'{end_point}users/{id}').json()
    name = response["name"]
    print('Employee {} is done with tasks'.format(name), end="")

    todos = requests.get(f'{end_point}todos?userId={id}').json()
    #print(todos)
    complete = []
    for todo in todos:
        if todo['completed'] is True:
            complete.append(todo)
    print('({}/{}):'.format(len(complete), len(todos)))
    for task in complete:
        print('\t {}'.format(task['title']))