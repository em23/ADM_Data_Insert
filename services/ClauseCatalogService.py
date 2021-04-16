import requests

from utils.load_jsons import get_clauses_data, get_controls_data


class ClauseCatalogService:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__base_url = f"http://{self.__host}:{self.__port}"

    def populate_db(self):
        self.populate_clauses()
        self.populate_controls()

    def populate_clauses(self):
        data = get_clauses_data()
        for clause in data:
            self.__post_clause(clause)

    def populate_controls(self):
        data = get_controls_data()
        for control in data:
            self.__post_controls(control)

    def __post_clause(self, clause):
        endpoint = f"{self.__base_url}/clauses"
        r = requests.post(url=endpoint, json=clause)
        print("The pastebin URL is:%s" % r.text)

    def __post_controls(self, control):
        endpoint = f"{self.__base_url}/controls"
        r = requests.post(url=endpoint, json=control)
        print("The pastebin URL is:%s" % r.text)
