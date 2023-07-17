import pandas as pd

df = pd.read_csv("coupons.csv")
# df.info()

# List of columns that we would like to explore
unique_weather = df['weather'].unique()
unique_income = df['income'].unique()
unique_education = df['education'].unique()
unique_destination = df['destination'].unique()
unique_passanger = df['passanger'].unique()
unique_time = df['time'].unique()
unique_expiration = df['expiration'].unique()
unique_age = df['age'].unique()
unique_gender = df['gender'].unique()


column_dict = [
    {"label": "Weather", "id": "weather_dropdown", "values": unique_weather},
    {"label": "Income", "id": "income_dropdown", "values": unique_income},
    {"label": "Education", "id": "education_dropdown", "values": unique_education},
    {"label": "Destination", "id": "destination_dropdown", "values": unique_destination},
    {"label": "Passanger", "id": "passanger_dropdown", "values": unique_passanger},
    {"label": "Time", "id": "time_dropdown", "values": unique_time},
    {"label": "Expiration", "id": "expiration_dropdown", "values": unique_expiration},
    {"label": "Age", "id": "age_dropdown", "values": unique_age},
    {"label": "Gender", "id": "gender_dropdown", "values": unique_gender},
]

column_list = ['weather',
               'income',
               'education',
                'destination',
               'passanger',
               'time',
               'expiration',
               'age',
               'gender'
               ]

column_names ={
    "weather": "Weather",
    "income" : "Income",
    "education" : "Education",
    "destination" : "Destination",
    "passanger" : "Passanger",
    "time" : "Time",
    "expiration" : "Expiration",
    "age" : "Age",
    "gender": "Gender"
}

column_dict2 = [
    {"label": "Weather", "id": "weather"},
    {"label": "Income", "id": "income"},
    {"label": "Education", "id": "education"},
    {"label": "Destination", "id": "destination"},
    {"label": "Passanger", "id": "passanger"},
    {"label": "Time", "id": "time"},
    {"label": "Expiration", "id": "expiration"},
    {"label": "Age", "id": "age"},
    {"label": "Gender", "id": "gender"}
    ]
