from typing import Optional
from google.cloud import datastore

datastore_client = datastore.Client()
TABLE_NAME = 'users'

def set_table_name(table_name):
    TABLE_NAME = table_name

def store_user(email, token):
    entity = datastore.Entity(key=datastore_client.key(TABLE_NAME))
    entity.update({
        'email': email,
        'token' : token
    })

    update_entity(entity)

def update_entity(user):
    datastore_client.put(user)

def fetch_user(email: Optional[str] = None, token: Optional[str] = None):
    query = datastore_client.query(kind=TABLE_NAME)
    if email:
        query.add_filter("email", "=", email)
    if token:
        query.add_filter("token", "=", token)
    return list(query.fetch())
