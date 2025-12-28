import requests
import json

api_key = None
with open('mping-api-key.txt') as f:
    api_key = f.read()

print(api_key)

# Set up our request headers indicating we want json returned and include
# our API Key for authorization.
# Make sure to include the word 'Token'. ie 'Token yourreallylongapikeyhere'
reqheaders = {
    'content-type':'application/json',
    'Authorization': f'Token {api_key:s}'
    }
reqparams = {
    'category':'Rain/Snow',
    'year':'2025',
    'month':'12',
    'day':'27'
}

url = 'http://mping.ou.edu/mping/api/v2/reports'
response = requests.get(url, params=reqparams, headers=reqheaders)

if response.status_code != 200:
    print('Request Failed with status code %i' % response.status_code)
else:
    print('Request Successful')
    dump = response.json()
    # Pretty print the data
    print(json.dumps(dump,indent=4))
    print(len(dump))

    data = json.loads(json.dumps(dump,indent=4))

    print(data['results'][0])