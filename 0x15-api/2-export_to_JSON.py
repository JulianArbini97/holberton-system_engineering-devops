#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ First we get the USER_ID """
    user_id = argv[1]

    """ Second we get the user name """
    all_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    user_name = all_info.json()
    user_name = user_name.get('username')

    """ Third we get the status of completition of tasks """
    status = []
    at = requests.get('https://jsonplaceholder.typicode.com/todos//?userId={}'
                      .format(argv[1]))
    ATPU_json = at.json()
    print(ATPU_json)
    for task in ATPU_json:
        results = task.get('completed')
        status.append(results)

    """ Fourth we get the task titles """
    titles = []
    at = requests.get('https://jsonplaceholder.typicode.com/todos//?userId={}'
                      .format(argv[1]))
    ATPU_json = at.json()
    for task in ATPU_json:
        title = task.get('title')
        titles.append(title)

    """ Creation of a counter to write in CSV file """
    len_list = 0
    for each in titles:
        len_list += 1

    """ Finally we export it to the json file """
    info_list = []
    json_dict = {}
    with open('{}.json'.format(argv[1]), mode="w") as json_file:
        for i in range(0, len_list):
            dict_PERtask = {}
            dict_PERtask['task'] = titles[i]
            dict_PERtask['completed'] = status[i]
            dict_PERtask['username'] = user_name
            info_list.append(dict_PERtask)

        json_dict["{}".format(user_id)] = info_list
        json.dump(json_dict, json_file)
