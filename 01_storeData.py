####################
# store data with json

"""store some numbers."""
import json

name = input("Whats your name?")
number = input("Whats your favorite number?")

filename = 'user.json'
with open(filename,'w') as f_obj:
    json.dump(name, f_obj)
    json.dump(number, f_obj)

# filename = 'user.json'
# with open(filename,'w') as f_obj:
#     json.dump(name, f_obj)
#     json.dump(number, f_obj)
