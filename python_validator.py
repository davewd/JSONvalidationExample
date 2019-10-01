import jsonschema
import simplejson as json
import os
import pathlib

print(os.getcwd())

with open('schema.json', 'r') as f:
    schema_data = f.read()
schema = json.loads(schema_data)

json_obj = {"name": "eggs", "price": 21.47}
print(jsonschema.validate(json_obj, schema))

json_obj = {"name": "eggs", "price": "blue"}
print(jsonschema.validate(json_obj, schema))

json_obj = {"name": "eggs", "price": -1}
print(jsonschema.validate(json_obj, schema))