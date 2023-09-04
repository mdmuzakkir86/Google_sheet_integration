'''
    Important Note please collect the required details before going with code.
    Requirements:
    1. CLIENT_ID
    2. CLIENT_SECRET
    3. spreadsheet_id
    4. refresh_token

    Follow below document to get above details later replace your deatils in code
    https://drive.google.com/drive/folders/14xoaR1poX9bLLHlPxuNH0rHmNhfupaq8
'''


import requests
import json


# API required variables
CLIENT_ID ='599682291270-tbn2ri6mb18jh06mbr0e23glr2e56ru3.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REFRESH_TOKEN = '1//04LCA5lWHc0mCCgYIARAAGAQSNwF-L9IrrUfY1T6eUvtGY5NiAqMRpYKr5TPCW5cBq9_PaSGB1uCc504l-8mnNTThptGkilclaLU'
spreadsheet_id = '1iK8rNzOlYPvngiAu4xNZEBp7nlLMRofrTGlQhl1Cfy0'


token_url = 'https://oauth2.googleapis.com/token'
ACCESS_TOKEN = None


def google_sheet_integration():
    print("Inside custom handler")
    data={
    'grant_type': 'refresh_token',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'refresh_token':REFRESH_TOKEN
    }
    refresh_response = requests.post(token_url, data=data)
    print('REFRESH_RESPONSE', refresh_response.json())
    fresh_response = json.loads(refresh_response.text)
    print(type(fresh_response))
    ACCESS_TOKEN = fresh_response['access_token']

    print("ACCESS_TOKEN in export:", ACCESS_TOKEN)
    data = {'Name':'Muzakkir', 'Location':'Mahbububnagar'}

    values = [
        [
        data.get('Name', ''),
        data.get('Location', ''),
        ]
    ]
    range_name = 'Sheet1!A1:B2'
    url =    f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}:append?valueInputOption=USER_ENTERED'
    headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
    }
    body = {
    'values': values
    }
    # Send the request to append the data to the sheet
    response = requests.post(url, headers=headers,
    data=json.dumps(body))
    print('GET_RESPONSE:',response.json())
    print(response.status_code)
    return input

google_sheet_integration()