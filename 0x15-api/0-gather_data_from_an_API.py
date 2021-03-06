#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import requests
import sys
if __name__ == "__main__":
    id = sys.argv[1]
    x = 0
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(id)).json()
    tasks = []
    for n in todos:
        if n.get('completed') is True:
            tasks.append(n['title'])
            x += 1
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), x, len(todos)))

    for n in tasks:
        print("\t {}".format(n))
