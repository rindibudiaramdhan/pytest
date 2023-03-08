import requests, json, os
from dotenv import load_dotenv

load_dotenv()

BASE_URL=os.getenv('JSA_BASE_URL', 'http://localhost:30004')
header = {
        'Api-Key': os.getenv('API_KEY', 'API_KEY')
    }

def get_token():
    KC_URL = os.getenv('KC_URL', 'localhost')
    KC_REALM = os.getenv('KC_REALM', 'kcrealm')
    KC_CLIENT_ID = os.getenv('KC_CLIENT_ID', 'kcclientid')
    KC_CLIENT_SECRET = os.getenv('KC_CLIENT_SECRET', 'kcclientsecret')
    KC_GRANT_TYPE = os.getenv('KC_GRANT_TYPE', 'kcgranttype')

    url = str(KC_URL) + "/realms/" + str(KC_REALM) + "/protocol/openid-connect/token"
    return requests.post(f'{url}', headers=header, data={
        'username': os.getenv('JSA_USERNAME'),
        'password': os.getenv('JSA_PASSWORD'),
        'grant_type': KC_GRANT_TYPE,
        'client_id': KC_CLIENT_ID,
        'client_secret':KC_CLIENT_SECRET
    })

def test_kendaraan_saya_unauthorized():
    url = BASE_URL + '/v1/pajak/kendaraan/kendaraan-saya'
    payloads = {
        'nik': os.getenv('USER_NIK'),
    }
    r = requests.post(f'{url}', headers=header, data=json.dumps(payloads))
    assert r.status_code == 401
    response = r.json()
    assert response.get('status') == False

def test_kendaraan_saya_success():
    url = BASE_URL + '/v1/pajak/kendaraan/kendaraan-saya'
    payloads = {
        'nik': os.getenv('USER_NIK'),
    }
    login = get_token()
    json_token = login.json()
    header['Authorization'] = 'Bearer ' + json_token.get('access_token')
    r = requests.post(f'{url}', headers=header, data=json.dumps(payloads))
    assert r.status_code == 200
    response = r.json()
    assert response.get('status') == True

