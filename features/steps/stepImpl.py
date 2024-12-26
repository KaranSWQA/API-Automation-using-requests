import requests
from behave import *
from Utilities.resources import *
from payLoad import *
from Utilities.configuration import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.payLoad = addBodypayload("FYJCS", 129668);


@when('we execute the AddBook Post API method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad)


@then('Book is sucessfully added')
def step_impl(context):
    print(context.response.json())
    new = context.response.json()
    context.k = new['ID']
    print(context.k)
    assert new["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.payLoad = addBodypayload(isbn, aisle);

@given('I have github auth credentails')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ("karanshetty1441994@gmail.com", getPassword())

@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo, verify=False, )


@then(u'status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code==200

