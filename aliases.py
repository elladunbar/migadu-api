#!/usr/bin/env uv run

import json
import os
import sys

import requests
from dotenv import load_dotenv


HEADERS = {'Content-Type': 'application/json'}
load_dotenv()
MIGADU_DOMAIN = os.getenv('MIGADU_DOMAIN')
MIGADU_USER = os.getenv('MIGADU_USER')
MIGADU_KEY = os.getenv('MIGADU_KEY')
URL = 'https://api.migadu.com/v1/domains/' + MIGADU_DOMAIN + '/aliases'
AUTH = (MIGADU_USER, MIGADU_KEY)
data = {'destinations': 'me@' + MIGADU_DOMAIN}


def print_as_json(jsonable):
    return print(json.dumps(jsonable, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Must provide the name of one alias to be created!")

    data['local_part'] = sys.argv[1]
    response = requests.post(URL, auth=AUTH, json=data, headers=HEADERS)
    if response.status_code != 200:
        print(f"Alias creation failed for {sys.argv[1]}")
