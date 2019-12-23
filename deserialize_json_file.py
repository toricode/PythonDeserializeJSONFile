import json

with open('D:\ToriCode\Python\contacts.json', 'r') as f:
    json_data = f.read()

contact_list = json.loads(json_data)

print("Object type: ", type(contact_list))

for contact in contact_list:
    print(contact)
