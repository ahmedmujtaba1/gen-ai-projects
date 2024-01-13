import requests

## Creating Users Code
# form = {
#     'username' : 'ahmed',
#     'password' : 'pakistan'
# }
# r = requests.post('http://127.0.0.1:8000/users/', json=form)
# print(r.json())

# Token Generator
data = {
    'username': 'ahmed',
    'password': 'pakistan',
}

r = requests.post('http://127.0.0.1:8000/token', data=data)

print(r.json())
