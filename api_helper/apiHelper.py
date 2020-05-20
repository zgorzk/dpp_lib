import requests
from requests.exceptions import HTTPError


class apiHelper(object):
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def getEntriesOnAuthorPk(self, authorPk):
        try:
            response = requests.get("https://api.e-science.pl/api/azon/authors/entries/" +
                                    str(authorPk) + "/",
                                    headers={'X-Api-Key': self.apiKey})
            response.raise_for_status()
            json_data = response.json()
            return json_data['results']
        except HTTPError as err:
            print(err)

    def getEntriesByPage(self, page):
        try:
            response = requests.get("https://api.e-science.pl/api/azon/entry/filter/?limit=100&offset=" +
                                    str(page) +
                                    "00", headers={'X-Api-Key': self.apiKey})
            response.raise_for_status()
            json_data = response.json()
            return json_data['results']
        except HTTPError as err:
            print(err)

    def getResultDetails(self, json):
        try:
            response = requests.get("https://api.e-science.pl/api/azon/entry/" +
                                    str(json['entry_type']) + "/",
                                    headers={'X-Api-Key': self.apiKey})
            response.raise_for_status()
            json_data = response.json()
            return json_data['results']
        except HTTPError as err:
            print(err)

    def getProgrammingLanguages(self):
        try:
            response = requests.get("https://api.e-science.pl/api/azon/programminglanguages/",
                                    headers={'X-Api-Key': self.apiKey})
            response.raise_for_status()
            json_data = response.json()
            return json_data['results']
        except HTTPError as err:
            print(err)
