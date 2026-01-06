import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# === 1. Google Sheets Auth ===
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)
client = gspread.authorize(creds)

# === 2. Open the Sheet ===
sheet = client.open("Grimoire Predictions").sheet1  # first tab

# === 3. Load Data ===
df = pd.read_csv("data/todays_betting_edges.csv")

# === 4. Export to Google Sheets ===
sheet.clear()
sheet.update([df.columns.values.tolist()] + df.values.tolist())

print("✅ Exported to Google Sheets: Grimoire Predictions")
