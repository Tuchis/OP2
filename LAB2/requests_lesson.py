import requests
import pprint
import urllib
import json

response = requests.request("GET", "http://lpnu.ua")
print(response)
print(response.headers['Content-Type'])

# https://httpbin.org

# GET
response = requests.get('http://httpbin.org/get')
response.text
response.encoding
response.content
response.url
response.status_code
response.headers
response.headers['Content-Type']
json_response = response.json()
pprint.pprint(json_response)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.get('http://httpbin.org/get', params=payload)
response.url

# POST
# Message Body
response = requests.post('https://httpbin.org/post', data={'key':'value'})
print(response)

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])
print(response.request.body)

#inspect their responses
response = requests.head('https://httpbin.org/get')
print(response.headers['Content-Type'])

response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])

# API
# url = "https://imdb8.p.rapidapi.com/title/get-filming-locations"
#
# querystring = {"tconst":"tt0944947"}
#
# headers = {
#     'x-rapidapi-host': "imdb8.p.rapidapi.com",
#     'x-rapidapi-key': "INBLmKEwUcmshIaVn0gHdGwwVhGgp1pkpWCjsnb0SsZz6uMdwy"
#     }
#
# # requesrs using
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(type(response), response.text)
# pprint.pprint(response.json())
# print(type(response.json()))
#
# print("______________________________________")
#
# # urllib using
# params = urllib.parse.urlencode(querystring)
# full_url = url+"?"+params
#
# req = urllib.request.Request(full_url, headers=headers)
# response = urllib.request.urlopen(req)
#
# print(type(response))
#
# data = response.read().decode(response.info().get_param('charset') or 'utf-8')
# data = json.loads(data)
# print(type(data))
#
# pprint.pprint(data)
#
# #response = requests.get('https://api.github.com/events')
