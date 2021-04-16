import json


def get_controls_data():
    with open("assets/controls.json", encoding='utf8') as f:
        data = json.load(f)
    return data


def get_clauses_data():
    with open("assets/clause.json", encoding='utf8') as f:
        data = json.load(f)
    return data
