#!/usr/bin/env python3
# THIS FILE WILL BE OVERWRITTEN. DO NOT MAKE ANY CHANGES HERE

import atexit
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# This is the Zip file you downloaded
SECURE_CONNECT_BUNDLE = '/workspace/bootcamp-fullstack-apps-with-cassandra/secure-connect-workshops.zip'
# This is the "Client Id" value you obtained earlier
USERNAME = "sPxAFZKmjlqYMZIeGvlmMhfo"
# This is the "Client Secret" value you obtained earlier
PASSWORD = "Nob,bS,9HX.e1Hj+2q.2FH4M4wUtFUvx-8l-tyYK6Wk,wb0zc3A-K7,T8.spPll7jESY5_f1hCUc46ijy8yByFTn5d94k3JBKX96WewOe.5Jf+_RiedYNdR4eloICWBY"
# This is the keyspace name
KEYSPACE = "todos"


secure_connect_bundle = SECURE_CONNECT_BUNDLE
path_to_creds = ''
cluster = Cluster(
    cloud={
        'secure_connect_bundle': SECURE_CONNECT_BUNDLE
    },
    auth_provider=PlainTextAuthProvider(USERNAME, PASSWORD)
)
session = cluster.connect(KEYSPACE)


@atexit.register
def shutdown_driver():
    cluster.shutdown()
    session.shutdown()
