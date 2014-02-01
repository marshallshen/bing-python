import unittest
import httpretty
import requests

from nose.tools import *
from bing.client import BingClient

def test_url():
    client = BingClient('account_key')
    assert_equal(client.url('foo'),
                'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=%27foo%27&$top=10&$format=json')

JSON_RESPONSE = '{"d":{"results":[{"__metadata":{"uri":"https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=\u0027Miscrosoft\u0027&$skip=0&$top=1","type":"WebResult"},"ID":"0e93973f-abdd-4858-95d9-df605c854480","Title":"Microsoft US | Devices and Services","Description":"At Microsoft our mission and values are to help people and businesses throughout the world realize their full potential.","DisplayUrl":"www.microsoft.com/en-us","Url":"http://www.microsoft.com/en-us/default.aspx"}],"__next":"https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=\u0027Miscrosoft\u0027&$skip=1&$top=1"}}'
def test_http_requests():
    httpretty.enable()  # enable HTTPretty so that it will monkey patch the socket module

    test_url = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=%27Microsoft%27&$top=10&$format=json'
    httpretty.register_uri(httpretty.GET, test_url,
                         body=JSON_RESPONSE,
                         content_type="application/json")

    response = BingClient('account_key').search('Microsoft')
    expected_response = [{'URL': 'http://www.microsoft.com/en-us/default.aspx',
                          'Summary': 'At Microsoft our mission and values are to help people and businesses throughout the world realize their full potential.',
                          'Title': 'Microsoft US | Devices and Services'}]

    assert_equal(response, expected_response)
    httpretty.disable()
    httpretty.reset()

