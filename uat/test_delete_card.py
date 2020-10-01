import requests

import json

def test_delete_card_json():
    """ For an existing user, it should return a list of card."""
    url = 'http://127.0.0.1:8000/users/9123/cards/b479de46-03f8-11eb-9ac0-3c15c2c07228'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.delete(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['id'] == 'b479de46-03f8-11eb-9ac0-3c15c2c07228' 
        
    # print response full body as text
    print(resp.text)



def test_delete_card_json_404_user():
    """ For non existing user, it should return a 404 error"""
    url = 'http://127.0.0.1:8000/users/NOTEXISTING/cards/bbba9f6a-03f8-11eb-9ac0-3c15c2c07228'
    
    resp = requests.delete(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 404
    # print response full body as text
    print(resp.text)

def test_delete_card_json_404_card():
    """ For non existing user, it should return a 404 error"""
    url = 'http://127.0.0.1:8000/users/9123/cards/NOTEXISTING'
    
    resp = requests.delete(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 404
    # print response full body as text
    print(resp.text)
