import requests
import json

def test():
    resp = requests.post('http://127.0.0.1:8000/api/abort/',
                     data=json.dumps({'abort': True}),
                     headers={'Content-Type':'application/json'})

test()