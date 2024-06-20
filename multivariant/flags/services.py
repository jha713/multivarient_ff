import requests

API_KEY = '4ee6bfa5-8de0-4bca-bb6c-d0cc5f8e8ed5'
BASE_URL = 'https://app.harness.io/gateway/api/v1/features'

def get_feature_flag_status(identifier):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    response = requests.get(f'{BASE_URL}/{identifier}', headers=headers)
    return response.json()

def get_multivariant_flag():
    # Example for getting a multivariant flag
    flag_data = get_feature_flag_status('multivariant_ff')
    return flag_data
