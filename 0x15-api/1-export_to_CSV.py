#!/usr/bin/python3
"""export data in the CSV format
"""
import csv
import requests
import sys
if __name__ == "__main__":
    id = sys.argv[1]
    x = 0
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(id)).json()
    with open("{}.csv".format(id), 'w') as CVSfile:
        writer = csv.writer(CVSfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for line in todos:
            writer.writerow([id, user.get('username'),
                            line.get('completed'), line.get('title')])
