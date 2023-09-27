import json
import jsonschema


class JsonValidator:

    def __init__(self, schema_file, schema_integrity_file):
        with open(schema_file, 'r') as schema_f:
            self.schema = json.load(schema_f)

        with open(schema_integrity_file, 'r') as integrity_f:
            self.schema_integrity = json.load(integrity_f)

    def validate_schema(self, json_file):
        try:
            with open(json_file, 'r') as json_f:
                json_data = json.load(json_f)
                # Validate against the schema
                jsonschema.validate(json_data, self.schema)
                # Perform additional custom validations based on schema integrity rules
                if self._custom_validate(json_data):
                    return True
                else:
                    return False
        except jsonschema.exceptions.ValidationError as e:
            print(f"JSON Schema Validation Error: {e}")
            return False
        except Exception as e:
            print(f"An error occurred while validating: {e}")
            return False

    def _custom_validate(self, json_data):
        return True



validator = JsonValidator('schema.json', 'schema_integrity.json')
result = validator.validate_schema('data.json')
if result:
    print("Validation succeeded")
else:
    print("Validation failed")