[![Coverage Status](https://coveralls.io/repos/github/KennHinga/kura_API/badge.svg?branch=develop)](https://coveralls.io/github/KennHinga/kura_API?branch=develop)
[![Build Status](https://travis-ci.org/KennHinga/kura_API.svg?branch=develop)](https://travis-ci.org/KennHinga/kura_API)
[![Maintainability](https://api.codeclimate.com/v1/badges/44905455b9aa25cc941e/maintainability)](https://codeclimate.com/github/KennHinga/kura_API/maintainability)

# kura_API

The API endpoints should respond with a JSON object specifying the HTTP status code, and
either a data property (on success) or an error property (on failure). When present, the data
property is always an array, even if there’s none, one, or several items within it

###Heroku link

[https://piga-kura.herokuapp.com/api/v1]

## Brief Description

Kura is an app that enables people to vote online

### Pivotal Tracker Board

[https://www.pivotaltracker.com/n/projects/2241639]

### Deploy

run in postman

### Pre-requisites

1. Python 2.7
2. Flask
3. Postman
 

### Getting started

Clone this repository [https://github.com/KennHinga/Kura.git]


Navigate to the cloned repository
`cd kura_API-API-v1`

### Installation

Create a virtual environment

`\Python27\Scripts\virtualenv.exe venv`

Activate the virtual environment

`venv/Scripts/activate`


Switch to 'develop' branch

`git checkout develop`

Install requirements

`pip install -r requirements.txt`

Run the application

` run.py`

### Testing

Run this command on the terminal/cmd

`pytest`

### Endpoints

| Endpoint                            |                   Functionality                    |
| ----------------------------------- | :------------------------------------------------: |
| POST/partyList                      |               Create a party                       |
| GET/partyList/<id>                  |             Fetch a specific party                 |
| GET/partyList                       |               Fetch all parties                    |
| PATCH/partyList/<id>               |               edit a specific party                |
| DELETE/PartyList/<id>               |               deletes a specific party             |
| POST/officeList                     |               creates an office                    |
| GET/officeList                      |                fetch all offices                   |
| GET/officeList/<id>                 |            fetch a specific office                 |


### Authors

# Kenn Hinga


