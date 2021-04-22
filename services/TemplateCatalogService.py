import requests

from utils.load_jsons import get_templates_data


class TemplateCatalogService:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__base_url = f"http://{self.__host}:{self.__port}"

    def populate_db(self):
        self.populate_templates()

    def populate_templates(self):
        data = get_templates_data()
        for item in data:
            self.__post_template(item)

    def __post_template(self, template):
        endpoint = f"{self.__base_url}/templates"
        r = requests.post(url=endpoint, json=template)
        print("The pastebin URL is:%s" % r.text)
