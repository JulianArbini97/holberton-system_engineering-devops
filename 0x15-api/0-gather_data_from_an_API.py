#!/usr/bin/python3
""" Program that returns information about his/her TODO list progress """
import requests
from sys import argv

if __name__ == "__main__":
    """ First we are going to find the name """
    all_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    user_name = all_info.json()
    user_name = user_name.get('name')

    """ Second we see how many tasks """
    total_tasks = 0
    at = requests.get('https://jsonplaceholder.typicode.com/todos//?userId={}'
                      .format(argv[1]))
    ATPU_json = at.json()
    for task in ATPU_json:
        total_tasks += 1

    """ Third we get the amount of tasks completed """
    completed_tasks = 0
    for task in ATPU_json:
        result = task.get('completed')
        if result is True:
            completed_tasks += 1

    """ Finally, we get all the completed tasks """
    completed_list = []
    for task in ATPU_json:
        result = task.get('completed')
        if result is True:
            title = task.get('title')
            completed_list.append(title)

    """ Printing result """
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed_tasks, total_tasks))
    for title in completed_list:
            print("\t {}".format(title))
