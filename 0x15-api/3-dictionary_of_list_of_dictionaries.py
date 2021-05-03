#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests

if __name__ == "__main__":
    final_json_dict = {}
    url_page = 'https://jsonplaceholder.typicode.com'
    all_info = requests.get('{}/users'.format(url_page))
    all_info = all_info.json()
    for each in all_info:
        id = each.get('id')

        all_info = requests.get('{}/users/{}'.format(url_page, id))
        user_name = all_info.json()
        user_name = user_name.get('username')

        status = []
        at = requests.get('{}/todos//?userId={}'.format(url_page, id))
        ATPU_json = at.json()
        for task in ATPU_json:
            results = task.get('completed')
            status.append(results)

        titles = []
        at = requests.get('{}/todos//?userId={}'.format(url_page, id))
        ATPU_json = at.json()
        for task in ATPU_json:
            title = task.get('title')
            titles.append(title)

        len_list = 0
        for each in titles:
            len_list += 1

        info_list = []
        json_dict = {}

        for i in range(0, len_list):
            dict_PERtask = {}
            dict_PERtask['task'] = titles[i]
            dict_PERtask['completed'] = status[i]
            dict_PERtask['username'] = user_name
            info_list.append(dict_PERtask)
        final_json_dict["{}".format(id)] = info_list

    with open('todo_all_employees.json', mode="w") as json_file:
        json.dump(final_json_dict, json_file)
