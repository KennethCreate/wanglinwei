import requests

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1', 'content-type': 'application/json'}
# r = requests.get(url, headers=headers)
r = requests.get('http://httpbin.org/get')

print(r.status_code)
print(r.headers)
