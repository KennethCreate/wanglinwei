import requests

s = requests.Session()
r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r2 = s.get("http://httpbin.org/cookies")
print(r2.text)
