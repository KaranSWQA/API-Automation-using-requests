import requests
from behave import *
from Utilities.resources import *
from payLoad import *
from Utilities.configuration import *


def after_scenario(context, scenario):
    if 'Library' in scenario.tags:
        url1 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        response_deleteBook = requests.post(url1, json={

            "ID": context.k}, )

        assert response_deleteBook.status_code == 200
        kar = response_deleteBook.json()
        print(kar['msg'])
        assert kar['msg'] == "book is successfully deleted"
