# Dejamobile Take Home - Backend

***For excercise purpose, do not use in prod.***

Implements a backend API for cards management.

##  API Endpoints

> GET /users/id/cards
> Return a list of digitalized card of a given user
> { cards: [{'id':UUID, 'hidden_pan':'1234...23'}, ...] }

> POST /users/id/cards { 'pan': '123456789012'}
> Add a digitalized pan for a given user
> { 'pan': '1234567891234567'}

> DEL /users/id/cards/uuid
> Delete a digitalized card for a user
> { 'id': uuid}

## How to use ?

### Prerequisite 

- Have python 3.8 installed
- Have `virtualenv` python package installed
- Clone this project into your workspace

### Initialize the project

This is a Python project. For good practices and environments isolation purpose, we advise to run it into a virtual envrionment.

```lang=bash
cd /path/to/djm_back
virtualenv .
source bin/activate
pip install -r requirements.txt
```

### Run the unit tests

Functions of this project are covered by unit tests. To execute them, please run this script

```lang=bash
cd /path/to/djm_back
source bin/activate
python -m unittest unit_tests/*.py
```

### Run the api

To run the API, you have to install it into its own environment. It creates an executable which starts the API server.

```lang=bash
cd /path/to/djm_back
source bin/activate
pip install -e .
djm-back --host 127.0.0.1 --ip 8000
```

It runs the API server listening on 127.0.0.1:8000.


### Run the UAT

To demonstrate the UAT, we implements simple UAT tests which can be runned with pytest.

Start a terminal and run the API *(See previous section.)*

Start a second terminal and run this script :

```lang=bash
cd /path/to/djm_back
source bin/activate
pytest uat/
```


### Use the sample of ci script

This script simulates a CI script which could be implements for GitlabCI, jenkins, ... CI/CD platforms. It :
- Initialize the virtualenv
- Run unit tests
- Build the wheel
- Deploy the app in background
- Run UAT tests

```lang=bash
cd /path/to/djm_back
bash ci_script.sh
```


