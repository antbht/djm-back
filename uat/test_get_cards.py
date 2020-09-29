import requests

import json

def test_get_user_cards_json():
    """ For an existing user, it should return a list of card."""
    url = 'http://127.0.0.1:8000/users/1234/cards'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.get(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body == [{'id':'9123456789123456', 'hidden_pan': 'XXXXXXXXXXXX1234'}]
    
    # print response full body as text
    print(resp.text)


def test_get_user_cards_err_404():
    """ For a non exisiting user, it should return a 404 error"""
    url = 'http://127.0.0.1:8000/users/NOTEXISTING/cards'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.get(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 404
    # print response full body as text
    print(resp.text)
