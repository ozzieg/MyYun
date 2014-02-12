__author__ = 'ozzie'

import httplib2
import urllib
import json

class SFClient:
    def __init__(self, options):
        self.client_id = options.get('client_id', None)
        self.client_secret = options.get('client_secret', None)
        self.username = options.get('username', None)
        self.password = options.get('password', None)
        self.security_token = options.get('security_token', '')
        self.login_server = options.get('login_server', 'https://login.salesforce.com')
        self.oauth = self.__get_token()

    def __get_token(self):
        token_url = '%s/services/oauth2/token' % self.login_server

        params = urllib.urlencode({
            'grant_type':'password',
            'client_id':self.client_id,
            'client_secret':self.client_secret,
            'username':self.username,
            'password':self.password+self.security_token
        })

        print 'Getting token from %s' % token_url

        try:
            h = httplib2.Http('.cache')
            resp, data = h.request(token_url, 'POST', params,
                             headers={'Content-Type':'application/x-www-form-urlencoded'})
        except httplib2.HttpLib2Error, e:
            print e

        print 'Got token %s' % data
        oauth = json.loads(data)
        print 'Logged into %s as %s' % (self.login_server, self.username)

        return oauth

    def get_oauth(self):
        return self.oauth
