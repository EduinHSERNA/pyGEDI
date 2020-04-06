#!/usr/bin/env python

try:
	import requests
except ImportError:
	sys.exit("""You need following module: requests """)


class sessionNASA(requests.Session): 
	AUTH_HOST = 'urs.earthdata.nasa.gov'

	def __init__(self, username, password):
		super().__init__() 
		self.auth = (username, password)
 
	def rebuild_auth(self, prepared_request, response): 
		headers = prepared_request.headers 
		url = prepared_request.url
		if 'Authorization' in headers: 
			original_parsed = requests.utils.urlparse(response.request.url) 
			redirect_parsed = requests.utils.urlparse(url) 
			if (original_parsed.hostname != redirect_parsed.hostname) and redirect_parsed.hostname != self.AUTH_HOST and original_parsed.hostname != self.AUTH_HOST: 
				del headers['Authorization']
		return
