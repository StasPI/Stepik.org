import requests

city = input('City? ')

api_url = 'http://api.openweathermap.org/data/2.5/weather/'

params = {
    'q': city,
    'appid': 'ce0ad98cb07c997ef297f35b91cfd348',
    'units': 'metric'
}

res = requests.get(api_url, params=params)

data = res.json()
template = 'Current temperature in {} is {}'

print(template.format(data['name'], data['main']['temp']))

# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.json())
