# Dejamobile Take Home - Backend

Implements a backend API.

Illustrate :
- Capacity of develop a software
- Capacity of desiging a REST API
- Importance of packaging
- TDD
- Deployment
- CI scripts

##  API Endpoints

> GET /users/id/cards
> Return a list of digitalized card of a given user
> { cards: [{'id':UUID, 'hidden_pan':'1234...23'}, ...] }

> POST /users/id/cards { 'pan': '123456789012'}
> Add a digitalized pan for a given user
> { 'id': UUID, 'hidden_pan': '1234...23'}

> DEL /users/id/cards/uuid
> Delete a digitalized card for a user
> { 'success': true}

## How to deploy ?

### Prerequires 

- Have python 3.8 installed with virtualenv

### Use the deployment script

- Open bash and execute deploy.sh

```
cd /path/to/project
bash deploy.sh
```

### Manual

```
cd /path/to/project
virtualenv .
source bin/activate
pip install -r requirements.txt
gunicorn ...
```

### Run unit-tests

```
cd /path/to/project
virtualenv .
source bin/activate
python run_tests.py
```


