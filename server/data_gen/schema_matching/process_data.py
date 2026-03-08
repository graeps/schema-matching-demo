# ruff: noqa: D415, D205, D100
import json
from statistics import mean
import numpy as np
import datetime
import string
import fastjsonschema
import uuid
from ..datagenlib.utils.type import get_type


def string_entity_properties(string_list: list[any], col_name: str) -> dict[any]:
    """Create properties from entity of string type
    :param string_list: list with values of string type
    :param col_name: name of the entity
    :return: dictionary of properties
    """
    clean_list = list(filter(lambda item: item is not None, string_list))
    length = len(clean_list)
    frac_letters = 0
    frac_upper = 0
    frac_lower = 0
    frac_spaces = 0
    frac_numbers = 0
    frac_others = 0
    num_null_values = 0
    min_length = None
    max_length = None
    for data in string_list:
        if data is None:
            num_null_values += 1
            continue
        data_length = len(data)
        data_frac_letters = 0
        data_frac_upper = 0
        data_frac_lower = 0
        data_frac_spaces = 0
        data_frac_numbers = 0
        data_frac_other = 0

        for ele in data:
            if ele.isalpha():
                data_frac_letters += 1
                if ele in string.ascii_lowercase:
                    data_frac_lower += 1
                else:
                    data_frac_upper += 1
            elif ele.isdigit():
                data_frac_numbers += 1
            elif ele.isspace():
                data_frac_spaces += 1
            else:
                data_frac_other += 1
        frac_letters += data_frac_letters / data_length
        frac_upper += data_frac_upper / data_length
        frac_lower += data_frac_lower / data_length
        frac_spaces += data_frac_spaces / data_length
        frac_numbers += data_frac_numbers / data_length
        frac_others += data_frac_other / data_length
        if min_length is None:
            min_length = data_length
            max_length = data_length
        elif data_length < min_length:
            min_length = data_length
        elif data_length > max_length:
            max_length = data_length

    dictionary_of_string_type = {
        "id": '"' + col_name + '"',
        "data_type": "string",
        "num_instances": len(string_list),
        "num_null_values": num_null_values,
        "min_length": min(map(len, clean_list)),  # len(min(clean_list, key=len)),
        "max_length": max(map(len, clean_list)),  # len(max(clean_list, key=len)),
        "avg_length": sum(map(len, clean_list)) / float(len(clean_list)),
        "frac_letter": frac_letters / length,
        "frac_upper": frac_upper / length,
        "frac_lower": frac_lower / length,
        "frac_space": frac_spaces / length,
        "frac_number": frac_numbers / length,
        "frac_other": frac_others / length
    }
    return dictionary_of_string_type


def number_entity_properties(number_list: list[any], col_name: str, data_type: str) -> dict[any]:
    """Create properties from entity of number type
    :param number_list: list with values of number type
    :param col_name: name of the entity
    :return: dictionary of properties
    """
    dictionary_of_number_type_entity = {
        "id": '"' + col_name + '"',
        "data_type": data_type,
        "num_instances": len(number_list),
        "num_null_values": number_list.count(None),
        "min_value": {""},
        "max_value": {""},
        "avg_value": {""},
        "standard_deviation": {""},
        "variance": {""}
    }
    output = list(filter(lambda item: item is not None, number_list))
    dictionary_of_number_type_entity["min_value"] = min(output)
    dictionary_of_number_type_entity["max_value"] = max(output)
    dictionary_of_number_type_entity["avg_value"] = mean(output)
    dictionary_of_number_type_entity["standard_deviation"] = np.std(output)
    dictionary_of_number_type_entity["variance"] = np.var(output)
    return dictionary_of_number_type_entity


def bool_entity_properties(bool_list: list[any], col_name: str) -> dict[any]:
    """Create properties from entity of boolean type
    :param bool_list: list with values of boolean type
    :param col_name: name of the entity
    :return: dictionary of properties
    """
    dictionary_of_boolean_type = {
        "id": '"' + col_name + '"',
        "data_type": "boolean",
        "num_instances": len(bool_list),
        "num_null_values": bool_list.count(None)
    }
    return dictionary_of_boolean_type


def object_entity_properties(object_list: list[any], col_name: str) -> dict[any]:
    """Create properties from entity of object type
    :param object_list: list with values of object type
    :param col_name: name of the entity
    :return: dictionary of properties
    """
    dictionary_of_object_data_type = {
        "id": '"' + col_name + '"',
        "data_type": "object",
        "num_instances": len(object_list),
        "num_null_values": object_list.count(None)
    }
    return dictionary_of_object_data_type


def date_entity_properties(date_to_convert: list[any], col_name: str) -> dict[any]:
    """Create properties from entity of date type
    :param date_to_convert: list with values of date type
    :param col_name: name of the entity
    :return: dictionary of properties
    """
    dictionary_of_date_type = {
        "id": '"' + col_name + '"',
        "data_type": "date",
        "num_instances": len(date_to_convert),
        "num_null_values": date_to_convert.count(None),
        "min_date": {""},
        "max_date": {""}}
    output = list(filter(lambda item: item is not None, date_to_convert))
    output = list(map(datetime.date.fromisoformat, output))
    dictionary_of_date_type["min_date"] = str(min(output))
    dictionary_of_date_type["max_date"] = str(max(output))
    return dictionary_of_date_type


def run_schema_creation(json_dict: json) -> dict[any]:
    """Travers through the json data and create schema with aggregated properties
    :param json_dict: dict of type json with data entry key point "entities"
    :return: schema with properties
    """
    out_dict = {}
    json_dict = json_dict.get('schema')
    column_names = json_dict.get("entities").keys()
    entity_array = []
    for column_name in column_names:
        data_type = json_dict.get("entities").get(column_name).get("data_type")
        inner_array = json_dict.get("entities").get(column_name).get("array")
        properties = None
        if data_type == "string":
            properties = string_entity_properties(inner_array, column_name)
        elif data_type in ["byte", "short", "integer", "long", "big_integer", "float", "double", "big_decimal"]:
            properties = number_entity_properties(inner_array, column_name, data_type)
        elif data_type == "boolean":
            properties = bool_entity_properties(inner_array, column_name)
        elif data_type == "date":
            properties = date_entity_properties(inner_array, column_name)
        elif data_type == "object":
            properties = object_entity_properties(inner_array, column_name)
        if properties is not None:
            entity_array.append(properties)
        else:
            print(f"entity properties in column {column_name} is empty - check data_type key {data_type}")
    out_dict["id"] = '"' + json_dict.get("id") + '"'
    out_dict["num_entities"] = len(entity_array)
    out_dict["entities"] = entity_array
    return out_dict


def validate_schemas(schema: json) -> bool:
    """Validate schema dictionary against schema template.
    :param schema: file to be validated against schema template
    :return: true if valid, otherwise false
    """
    validator = fastjsonschema.compile(json.load(open("resources/valid_schema_template.json")))
    try:
        validator(schema)
        return True
    except Exception as e:
        schema_name = schema.get("id")
        print(f"failed to validate schema: {schema_name}")
        print("Exception :" + str(e))
        return False


def process_data(schema_list: list) -> list[dict]:
    """Process a valid list of schemas to apply schema matching on
    :param schema_list: list of json schemas made with datagenlib
    :return: list of processed json schemas
    """
    processed_list = []

    # Validate that the schema_list is a non-empty list
    if not isinstance(schema_list, list) or not schema_list:
        print("Error: 'schema_list' must be a non-empty list.")
        return []

    for schema in schema_list:
        try:
            # Validate that the schema has the required 'data' attribute
            if not hasattr(schema, 'data') or not isinstance(schema.data, dict):
                print(f"Error: Each schema must have a 'data' attribute of type dict. Skipping schema: {schema}")
                continue

            uniq_ident = uuid.uuid4().hex

            # Create entity dictionary
            try:
                entity_dict = {
                    data: {"data_type": get_type(schema.data[data]), "array": schema.data[data]}
                    for data in schema.data
                }
            except Exception as e:
                print(f"Error processing schema data: {e}. Skipping schema: {schema}")
                continue
            # Prepare the processed schema as JSON
            processed_schema = json.loads(json.dumps(
                {
                    "id": uniq_ident,
                    "schema": {
                        "id": getattr(schema, 'id', 'unknown'),  # Ensure schema has an 'id' attribute
                        "entities": entity_dict
                    }
                },
                indent=4,
                sort_keys=True,
                default=str
            ))

            # Run schema creation
            try:
                created_schema = run_schema_creation(processed_schema)
            except Exception as e:
                print(f"Error in schema creation: {e}. Skipping schema: {processed_schema}")
                continue

            # Build the output schema
            output_schema = {
                "id": '"' + processed_schema.get('id', 'unknown') + '"',
                "num_schemas": 1,
                "schemas": [created_schema]
            }

            # Add the processed schema to the list
            processed_list.append(output_schema)
            print(f"Successfully processed schema: {output_schema['id']}")

        except Exception as e:
            print(f"Unexpected error processing schema: {e}. Skipping schema: {schema}")

    return processed_list
