import hy
import json
import os
from dotenv import load_dotenv
import requests
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
_hy_anon_var_1 = None
with open('needed_aliases.txt', 'r') as f:
    needed_aliases = tuple(map(lambda l: l.strip(), f.readlines()))
    _hy_anon_var_1 = None
for needed_alias in needed_aliases:
    data['local_part'] = needed_alias
    response = requests.post(URL, auth=AUTH, json=data, headers=HEADERS)
    print(needed_alias) if response.status_code != 200 else None
