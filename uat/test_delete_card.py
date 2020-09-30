import requests

import json

def test_delete_card_json():
    """ For an existing user, it should return a list of card."""
    url = 'http://127.0.0.1:8000/users/9123/cards/1234'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.delete(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['id'] == '1234' 
        
    # print response full body as text
    print(resp.text)



def test_delete_card_json_404_user():
    """ For non existing user, it should return a 404 error"""
    url = 'http://127.0.0.1:8000/users/NOTEXISTING/cards/1234'
    
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
