#!/usr/bin/python

import pprint
import requests

r = requests.get('https://api.github.com/users/heejaekkk')

if r.status_code == 200:

	json_data = r.json()
	pprint_pprint(json_data)
