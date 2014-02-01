# -*- coding: utf-8 -*-
# API Wrapper for Bing Search API
from __init__ import *

class BingClient(object):
    def __init__(self, account_key):
        self.auth = 'Basic %s' % (':%s' % account_key).encode('base64')[:-1] # Use basic auth

    def search(self, query):
        return self.parse(self.url(query))

    def url(self, query):
        query = urllib.quote(query)
        return BASE_URL+'?Query=%27'+query+'%27'+DEFAULT_PARAMS

    def formatted_resp(self, results_list):
        return [self.format_result(result) for result in results_list]

    def format_result(self, result):
        return {'URL': result['Url'].encode('ascii', 'ignore'),
                'Summary': result['Description'].encode('ascii', 'ignore'),
                'Title': result['Title'].encode('ascii', 'ignore')}

    def parse(self, url):
        request = urllib2.Request(url)
        request_opener = urllib2.build_opener()
        request.add_header('Authorization', self.auth)

        response = request_opener.open(request)
        response_data = response.read()
        json_result = json.loads(response_data)
        return self.formatted_resp(json_result['d']['results'])
