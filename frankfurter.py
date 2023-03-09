import requests
from strings import Strings
from pprint import pprint
from typing import List, Union, Optional

class FrankFurter:

    def __init__(self):
        self.__uri = Strings['API_URL']

    def __request(self, val: str):
        try:
            uri = self.__uri+val
            return requests.get(uri).json()
        except Exception as e:
            return e

    def latest(
        self, 
        frm: Optional[str]="EUR",
        to: Optional[Union[str, List]]=""
        ) -> json:
        return self.__request('latest')


f = FrankFurter()

pprint(f.latest())

