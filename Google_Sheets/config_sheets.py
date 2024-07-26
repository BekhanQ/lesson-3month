from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = "lesson_43_2.json"

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

google_sheet_id_users = '1PCd81KPwfGmtr9Mr0_gpvbbsJCI6ljcaFMYjXjYBPKA'

service = build('sheets', 'v4', credentials=creds)