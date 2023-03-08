import requests, json, os
from dotenv import load_dotenv

load_dotenv()

BASE_URL=os.getenv('JSA_BASE_URL', 'http://localhost:30004')
header = {
        'Api-Key': os.getenv('API_KEY')
    }

def test_info_kendaraan():
    url = BASE_URL + '/v1/pajak/kendaraan/info-kendaraan'
    payloads = {
        'noPolisi': os.getenv('PAJAK_NO_POLISI'),
        'kodePlat': os.getenv('PAJAK_KODE_PLAT'),
    }
    r = requests.post(f'{url}', headers=header, data=json.dumps(payloads))
