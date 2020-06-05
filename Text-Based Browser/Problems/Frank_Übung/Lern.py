import requests

r = requests.get('https://docs.python.org')
print(r)

if r:
    print('sucess')
else:
    print('Fail')

print(r.text)
print(r.headers['Content-Type'])