import requests

import json

def test_post_card_json():
    """ For an existing user, it should return a list of card."""
    url = 'http://127.0.0.1:8000/users/5678/cards'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, data='{"pan":"1234567891234567"}', headers={'content-type': 'application/json'})       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201
    resp_body = resp.json()
    assert len(resp_body) >= 2
    assert resp_body[-1]['hidden_pan'] == 'XXXXXXXXXXXX4567'
        
    # print response full body as text
    print(resp.text)


def test_post_card_json_400():
    """ For a bad formated request, it should return a 400 error"""
    url = 'http://127.0.0.1:8000/users/5678/cards'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, data='{}', headers={'content-type': 'application/json'})       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 400
    # print response full body as text
    print(resp.text)

def test_post_card_json_404():
    """ For non existing user, it should return a 404 error"""
    url = 'http://127.0.0.1:8000/users/NOTEXISTING/cards'
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, data='{"pan":"1234567891234567"}', headers={'content-type': 'application/json'})       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 404
    # print response full body as text
    print(resp.text)
