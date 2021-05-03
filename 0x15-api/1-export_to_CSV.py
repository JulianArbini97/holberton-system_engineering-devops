#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
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

    """ Finally we export it to the CSV file """
    with open('{}.csv'.format(user_id), mode="w") as csv_file:
        CSV_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for i in range(0, len_list):
            CSV_writer.writerow([user_id, user_name, status[i], titles[i]])
