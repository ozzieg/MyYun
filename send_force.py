#!/opt/python/bin/python
__author__ = 'ozzie'

import httplib2
import sf_client
import os

client = sf_client.SFClient({
    'client_id': os.environ['SF_CLIENT_ID'],
    'client_secret': os.environ['SF_CLIENT_SECRET'],
    'username': os.environ['SF_USERNAME'],
    'password': os.environ['SF_PASSWORD'],
    'login_server': os.environ['SF_LOGIN_SERVER'],
    'security_token': os.environ['SF_SECURITY_TOKEN']
})

j = client.get_oauth();
access_token = j['access_token']
instance_url = j['instance_url']

h = httplib2.Http('.cache')
resp, content = h.request(instance_url + '/services/data/v29.0/sobjects/Account/', "GET", headers={'Authorization':'Bearer '+access_token})
print resp, content