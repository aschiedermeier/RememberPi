""" load some previously stored numbers. """

import json

f_name = 'user.json'

try:
    with open(f_name) as f_obj:
        name = json.load(f_obj)
        number = json.load(f_obj)
except FileNotFoundError:
    msg = "Can't find {0}.".format(f_name)
    print(msg)
else:
    print ("Hello, %s! "% name) 
    print ("You like number %s! "% number) 
    