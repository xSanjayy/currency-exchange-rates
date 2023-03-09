import requests
from strings import Strings
from pprint import pprint
from typing import List, Union, Optional


class FrankFurter:

    def __init__(self):
        self.__uri = Strings['API_URL']

    def __request(self, val: str):
        try:
            uri = self.__uri + val
            return requests.get(uri).json()
        except Exception as e:
            return e

    def latest(
            self,
            frm: Optional[str] = "EUR",
            to: Optional[Union[str, List]] = ""
    ) -> dict:
        uri = "latest"
        if frm != "EUR":
            uri += f"?from={frm}"
        if type(to) is list:
            uri += f"&to={','.join(to)}"
        else:
            uri += f"&to={to}"
        # print(uri)
        return self.__request(uri)

    def convert(
            self,
            amount: int,
            frm: str,
            to: str
    ):
        uri = "latest"
        uri += f"?amount={amount}"
        uri += f"&from={frm}"
        uri += f"&to={to}"
        # print(uri)
        return self.__request(uri)

    def currencies(
            self
    ):
        return self.__request('currencies')

