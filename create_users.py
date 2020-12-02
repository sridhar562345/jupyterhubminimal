#!/usr/bin/env python
# -*- coding: utf-8 -*-

# - security endpoint
# - cloudant/couchdb interface

import os
import json
import logging
import requests
from cloudant import couchdb
from cloudant.error import CloudantClientException
from dotenv import load_dotenv


path_to_env_file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    ".env"
)
load_dotenv(path_to_env_file)
admin_username = os.getenv("COUCHDB_USER")
admin_password = os.getenv("COUCHDB_PASSWORD")

with couchdb(admin_username, admin_password, url="http://localhost:5984") as client:
    try:
        client.delete_database('users')
    except CloudantClientException:
        pass  # in case the database does not exist yet
    user_db = client.create_database("users")
    logging.debug("db 'users' created")

    # make admin read only
    logging.debug("make db 'users' read-only")
    security_endpoint = "http://{username}:{password}@{server_url}/users/_security".format(
        username=admin_username,
        password=admin_password,
        server_url="localhost:5984"
    )
    requests.put(security_endpoint, data=json.dumps({"admins":{"names":["admin"]},"members":{"names":["admin"]}}))
    logging.debug("db 'users' made read-only")

    # create users
    logging.debug("add users")
    data = {
        'username': "test",
        'password': "test"
    }
    user_db.create_document(data)
logging.debug("all users were sucessfully prepared")


