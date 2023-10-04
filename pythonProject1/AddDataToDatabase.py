import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-insight-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "11":
        {
            "name": "Elon Musk",
            "major": "SpaceX",
            "starting_year": 2001,
            "total_attedndace": 6,
            "standing": "Good",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },
    "2020AIFT1108088":
        {
            "name": "Jayash Kamdi",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
    "2020AIFT1108089":
        {
            "name": "HARIOM TIWARI",
            "major": "Cyber Security",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },
    "2020AIFT1108079":
        {
            "name": "ANSHU KUMAR",
            "major": "Web Devlopment",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },


"2020AIFT11011028":
        {
            "name": "Arpit Kharche",
            "major": "IT",
            "starting_year": 4,
            "total_attedndace": 10,
            "standing": "8.5",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },
    "2020AIFT1111027":
        {
            "name": "Aryan Chauhan",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
        "2020AIFT1101082":
        {
            "name": "Ashray Pillewan",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"
        },

        "2020AIFT1101083":
        {
            "name": "Ayush Sakle",
             "major": "Cyber Security",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },

            "2020AIFT1101109":
        {
            "name": "Bhojraj Padole",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
        "2020AIFT1101122":
        {
            "name": "Bhushan Gaiwat",
            "major": "DevOps",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
        "2020AIFT1101071":
        {
            "name": "Chaitany kuralkar",
            "major": "DevOps",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },
        "2020AIFT1101173":
        {
            "name": "Chetan Kumbhare",
             "major": "Cyber Security",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },
        "2020AIFT1101082":
        {
            "name": "Ashray Pillewan",
            "major": "DevOps",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"
        },
        "2020AIFT1101179":
        {
            "name": "Dev Mawley",
             "major": "Cyber Security",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },

        "2020AIFT1101213":
        {
            "name": "Dhairya Darda",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
        "2020AIFT1111037":
        {
            "name": "Divyanshu Sindapure",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
        "2020AIFT1111144":
        {
            "name": "Dushyant Bawanthade",
             "major": "DevOps",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        },
        "2020AIFT1101159":
        {
            "name": "Hariom Tiwari",
             "major": "Cyber Security",
            "starting_year": 2002,
            "total_attedndace": 10,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:34"

        },
        "2020AIFT1111020":
        {
            "name": "Harsh Rokade",
            "major": "AI",
            "starting_year": "IV",
            "total_attedndace": 6,
            "standing": "9.0",
            "year": 4,
            "last_attendence_time": "2023-06-11 00:54:3e"

        }
}
for key, value in data.items():
    ref.child(key).set(value)
