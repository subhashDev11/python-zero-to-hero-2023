#Request
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # should print 200 if the request was successful
print(response.content)  # should print the response body as bytes
print(response.text)  # should print the response body as a string


params = {'q': 'python requests'}
response = requests.get('https://www.google.com/search', params=params)
print(response.url)  # should print the full URL with query parameters
