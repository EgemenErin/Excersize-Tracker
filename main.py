import requests
import datetime
import os

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"].strip()
APP_ID = os.environ["APP_ID"].strip()
API_KEY = os.environ["API_KEY"].strip()

DATE = datetime.date.today()
GENDER = "male"
WEIGHT_KG = 74
HEIGHT_CM = 180
AGE = 21

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
sentence = input("Tell me which exercise you did? ")
parameters = {
"query": sentence,
"gender": GENDER,
"weight_kg": WEIGHT_KG,
"height_cm": HEIGHT_CM,
"age": AGE
}


response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

print(result)

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)
    print(sheet_response.text)
