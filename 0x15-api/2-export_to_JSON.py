#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import requests
import sys
import json
if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(id)).json()
    username = user.get('username')
    tasks = []
    for task in todos:
        jtask = {}
        jtask['task'] = task.get('title')
        jtask['completed'] = task.get('completed')
        jtask['username'] = username

    jsd = {}
    jsd['{}'.format(id)] = tasks

    with open('{}.json'.format(id), 'w') as f:
        json.dump(jsd, f)
