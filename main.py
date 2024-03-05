from data_to_json import DataToJson as dj
from get_user_city_url import GetUserCity as guc
from google_sheet_upload import GoogleSheetify as gs
import requests, json
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
from dotenv import load_dotenv

load_dotenv()

# CONSTANTS
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
GOOGLE_OAUTH_ID = os.environ.get('GOOGLE_OAUTH_ID')
GOOGLE_OAUTH_PWD = os.environ.get('GOOGLE_OAUTH_PWD')
GOOGLE_SERVICE_ACCOUNT = os.environ.get('GOOGLE_SERVICE_ACCOUNT')
SHEET_ID = os.environ.get('SHEET_ID')

searching = True
guc, dj, gs = guc(), dj(), gs()
while searching:
    # getting url of the selected city
    guc.get_city_list()
    guc.save_city_list()
    try:
        city_index, city_input = guc.user_input_city()
    except ValueError:
        break
    city_url = guc.click_city(city_index)
    # get and save chosen city's property data as json list
    dj.go_to_url(url=city_url)
    property_list = dj.property_data_to_list()
    property_dict = dj.property_list_to_dict(city_input)
    if not property_dict:
        continue
    dj.dump_json(city_input)

# transfer data to google spreadsheet
property_json = dj.load_json()
print(f'added data successfully\ndata added: {property_json}')
gs.send_to_sheet(property_json)
