from urlparse import urljoin
from urllib import urlencode
import urllib2, base64
import json


API_URL_DEFAULT = 'https://api.sqwiggle.com/'
FORMAT_DEFAULT = 'json'


class Sqwiggle(object):
    def __init__(self, token=None, url=API_URL_DEFAULT, format=FORMAT_DEFAULT):
        self.url = url
        self.token = token
        self.format = format
        self.opener = urllib2.build_opener(urllib2.HTTPSHandler())

    class RequestWithMethod(urllib2.Request):
        def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False, http_method=None):
            urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
            if http_method:
                self.method = http_method

        def get_method(self):
            if self.method:
                return self.method
            return urllib2.Request.get_method(self)

    def method(self, url, method="GET", parameters=None, timeout=None):
        method_url = urljoin(self.url, url)

        if method == "GET":
            if not parameters:
                parameters = dict()

            parameters['format'] = self.format

            query_string = urlencode(parameters)
            request_data = None
        else:
            query_parameters = dict()

            query_string = urlencode(query_parameters)

            if parameters:
                request_data = urlencode(parameters)
            else:
                request_data = None

        method_url = method_url + '?' + query_string

        req = self.RequestWithMethod(method_url, http_method=method, data=request_data)
        base64string = base64.encodestring('%s:X' % self.token).replace('\n', '')
        req.add_header("Authorization", "Basic %s" % base64string)

        response = self.opener.open(req, None, timeout).read()

        return json.loads(response)
