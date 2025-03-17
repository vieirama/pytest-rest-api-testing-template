import os
import json
from pathlib import Path
from jsonschema import validate

class SchemaValidation:
    def __init__(self, schema_file, response):
        self.schema = self.get_schema(schema_file)
        self.response = response

    def get_schema(self, schema_file):
        cwd = os.getcwd()
        schema_path = Path(cwd, 'schemas', schema_file).with_suffix('.json')

        with open(schema_path, 'r') as file:
            schema = json.load(file)
        
        return schema

    def validate_schema(self):
        validate(self.response, self.schema)
