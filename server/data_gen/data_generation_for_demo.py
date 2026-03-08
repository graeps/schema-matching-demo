# ruff: noqa: F405, F403
from flask import jsonify
import json

from .schema_matching import process_data as pd
from .schema_matching import schema_matching_lib_connector as connector
from .datagenlib.schemas import *
from .datagenlib.utils import AvailLang

schema_dict = {"Kunde": Customer,
               "Prominenter": Celebrity,
               "Konzert": Concert,
               "Kreditkarte": CreditCard,
               "Diabetes Patient": DiabetesPatient,
               "TikTok Nutzer": TikTokUser,
               "Wein Bewertung": WineReviews,
               "Film": Movie,
               "Autounfall": CarCrashes}

config_dict = {"einfach": 'simple_config.json',
               "optimal": 'opt_config.json'}


def create_random_schema(schema_choice: str, language_choice="Deutsch", number_entities=5, dirty=False) -> Schema:
    """Creates a random schema with randomly chosen entities to given schema choice contained in schema_dict.

    Args:
        schema_choice (str): key for schema based on schema_dict.
        language_choice (str): chosen language for schema. Default German. If not german then English will be used.
        number_entities (int): number of random entities (= columns of the table), Default 5.
        dirty (bool): whether the data should be dirty (= with missing data). Default False

    Returns: Schema object
    """
    schema = schema_dict[schema_choice]()
    entity_choice = schema.possible_entities[:number_entities]
    language = AvailLang.DE.value if language_choice == "Deutsch" else AvailLang.EN.value
    schema.create(num_instances=1000,
                  lang=language,
                  instance_lang=language,
                  entities=entity_choice,
                  dirty=dirty,
                  )
    return schema


def gen_data_from_request(option_choice, file_path):
    """Generates the representation of two schemas of same class using datagenlib to show them in the browser.

    Args:
        file_path: path to store results from data generation based on user session id.
        option_choice: json dict of the form {'schema': schema_choice, 'lang': language_choice}

    Returns:
        json dict of the form {'matching': matching_results, 'data': schema_data_shorted_for_browser}
    """
    try:
        # Generate data and matching if the attribute lists are not empty
        if option_choice:
            language_choice = option_choice["lang"]
            if language_choice != "gemischt":
                language1 = option_choice["lang"]
                language2 = option_choice["lang"]
            else:
                language1 = "Deutsch"
                language2 = "Englisch"

            schema_choice = option_choice["schema"]

            number_entities = 5
            schema1 = create_random_schema(schema_choice, language1, number_entities)
            schema2 = create_random_schema(schema_choice, language2, number_entities)
            schemas = pd.process_data([schema1, schema2])

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(schemas, file, indent=4)
            # Shorten the data of each column for representation in the browser
            data1_short = {key: schema1.data[key][:3] for key in schema1.data}
            data2_short = {key: schema2.data[key][:3] for key in schema2.data}
            output_tables = [{"title": schema1.id, "schema": data1_short}, {"title": schema2.id, "schema": data2_short}]
            # Return matching results and the data to be shown in the browser
            return jsonify({"data": output_tables})
        else:
            return "Both language_choice and schema_choice must be provided in the query parameters.", 400
    except Exception as e:
        return str(e), 500


def gen_matching_from_request(config_choice, file_path):
    """Generates the matching of two schemas using schema_matching_lib_connector to show it in the browser.

    Args:
        file_path: file_path to find data generation results based on user session id.
        config_choice: configuration file for schema_matching_lib_connector.match_schemas.

    Returns:
        json dict of the form {'matching': matching_results, 'data': schema_data_shorted_for_browser}
    """
    try:
        # Generate data and matching if the attribute lists are not empty
        if config_choice:
            config = config_dict[config_choice]
            # Load schema data from file
            with open(file_path) as file:
                schemas = json.load(file)

            print("--------------schema1 after saving to file----------------\n", schemas, flush=True)
            # Calculate matching under use of config file
            matching_result = connector.match_schemas(schemas, config)

            # Return matching results and the data to be shown in the browser
            return jsonify({"matching": matching_result})
        else:
            return "Config must be provided.", 400
    except Exception as e:
        return str(e), 500
