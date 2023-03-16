import requests
import json
base_url = 'https://petstore.swagger.io/v2'

status = 'available'

headers1 = {'accept': 'application/json', 'Content-Type': 'application/json'}

new_pet = {
    "id": 13598,
    "category": {
        "id": 2,
        "name": "beast"
    },
    "name": "cat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 13,
            "name": "faster"
        }
    ],
    "status": "available"
}


update_new_pet = {
    "id": 13598,
    "category": {
        "id": 2,
        "name": "string"
    },
    "name": "Kong",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 3,
            "name": "string"
        }
    ],
    "status": "sold"
}


res = requests.get( f"{base_url}/pet/findByStatus", params={'status': 'available'},
                    headers=headers1)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))




info_js = json.dumps(new_pet, ensure_ascii=False)

res = requests.post(f'{base_url}/pet', headers=headers1, data=info_js)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


info_js = json.dumps(update_new_pet, ensure_ascii=False)

res = requests.put(f'{base_url}/pet', headers=headers1, data=info_js)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


res = requests.delete(f'{base_url}/pet/{13598}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
