from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json

with open('schema.json') as file:
    schema = json.load(file)

with open('good.json') as file:
    good = json.load(file)

with open('bad.json') as file:
    bad = json.load(file)

try:
    validate(good, schema)
    print("good.json is OK")
except ValidationError as error:
    print("good.json is invalid: {0}".format(error))

try:
    validate(bad, schema)
    print("bad.json is OK")
except ValidationError as error:
    print("bad.json is invalid: {0}".format(error))