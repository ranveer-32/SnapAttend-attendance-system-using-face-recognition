import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-8565a-default-rtdb.firebaseio.com/"
})

# Reference to the database
ref = db.reference('Students')

# Data structure
data = {
    "Classes": {
        "ThirdYear": {
            "DAA": {
                "2223000123": {
                    "name": "Elon Musk",
                    "total_attendance": 0,
                    "last_attendance_time": "2024-04-28 00:54:34"
                },
                "2223000124":
                    {
                        "name": "Ratan Tata",
                        "Branch": "Mechanical",
                        "Year": "final",
                        "Roll No": "56",
                        "Division": "C",
                        "Batch": "C-2",
                        "PRN": "2223000124",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },

                "2223000598":
                    {
                        "name": "Ranveer Jogdande",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "32",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000598",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000654":
                    {
                        "name": "Mangal Kargonavar ",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "34",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000654",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000423":
                    {
                        "name": "Samiksha Kamble",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "24",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000423",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000508":
                    {
                        "name": "Sairaj Jadhav",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "30",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "22230000508",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },

                "2223000209":
                    {
                        "name": "Apurva Waghmode",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "9",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000209",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000320":
                    {
                        "name": "Shriyani Teli",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "18",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000320",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000073":
                    {
                        "name": "Vrishabh Firgan",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "1",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000073",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "22230000409":
                    {
                        "name": "Atharv Banne",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "26",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000409",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000690":
                    {
                        "name": "Vijaya Kunde",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "38",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000690",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000431":
                    {
                        "name": "Viraj Joshikar",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "1",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000431",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    }
            },
            "EDA": {"2223000123": {
        "name": "Elon Musk",
        "total_attendance": 0,
        "last_attendance_time": "2024-04-28 00:54:34"
      },
    "2223000124":
        {
            "name": "Ratan Tata",
            "Branch": "Mechanical",
            "Year": "final",
            "Roll No": "56",
            "Division": "C",
            "Batch": "C-2",
            "PRN": "2223000124",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },

    "2223000598":
        {
            "name": "Ranveer Jogdande",
            "Branch": "Data Science",
            "Year": "Third",
            "Roll No": "32",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000598",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000654":
        {
            "name": "Mangal Kargonavar ",
            "Branch": "Data Science",
            "Year": "Third",
            "Roll No": "34",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000654",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000423":
        {
            "name": "Samiksha Kamble",
            "Branch": "Data Science",
            "Year": "Third",
            "Roll No": "24",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000423",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000508":
        {
            "name": "Sairaj Jadhav",
            "Branch": "Data Science",
            "Year": "Third",
            "Roll No": "30",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "22230000508",
            "total_attendance": "0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },

    "2223000209":
        {
            "name": "Apurva Waghmode",
            "Branch": "Data Science",
            "Year": "Third",
            "Roll No": "9",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000209",
            "total_attendance": "0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000320":
        {
            "name": "Shriyani Teli",
            "Branch": "Data Science",
            "Year": "Third",
            "Roll No": "18",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000320",
            "total_attendance": "0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000073":
        {
            "name": "Vrishabh Firgan",
            "Branch": "Data Science",
            "Year": "THIRD",
            "Roll No": "1",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000073",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "22230000409":
        {
            "name": "Atharv Banne",
            "Branch": "Data Science",
            "Year": "THIRD",
            "Roll No": "26",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000409",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000690":
        {
            "name": "Vijaya Kunde",
            "Branch": "Data Science",
            "Year": "THIRD",
            "Roll No": "38",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000690",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        },
    "2223000431":
        {
            "name": "Viraj Joshikar",
            "Branch": "Data Science",
            "Year": "THIRD",
            "Roll No": "1",
            "Division": "A",
            "Batch": "A-1",
            "PRN": "2223000431",
            "total_attendance":"0",
            "last_attendance_time": "2024-04-28 00:54:34"
        }
            },
            "DBMS": {
                "2223000123": {
                    "name": "Elon Musk",
                    "total_attendance": 0,
                    "last_attendance_time": "2024-04-28 00:54:34"
                },
                "2223000124":
                    {
                        "name": "Ratan Tata",
                        "Branch": "Mechanical",
                        "Year": "final",
                        "Roll No": "56",
                        "Division": "C",
                        "Batch": "C-2",
                        "PRN": "2223000124",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },

                "2223000598":
                    {
                        "name": "Ranveer Jogdande",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "32",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000598",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000654":
                    {
                        "name": "Mangal Kargonavar ",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "34",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000654",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000423":
                    {
                        "name": "Samiksha Kamble",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "24",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000423",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000508":
                    {
                        "name": "Sairaj Jadhav",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "30",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "22230000508",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },

                "2223000209":
                    {
                        "name": "Apurva Waghmode",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "9",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000209",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000320":
                    {
                        "name": "Shriyani Teli",
                        "Branch": "Data Science",
                        "Year": "Third",
                        "Roll No": "18",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000320",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000073":
                    {
                        "name": "Vrishabh Firgan",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "1",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000073",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "22230000409":
                    {
                        "name": "Atharv Banne",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "26",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000409",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000690":
                    {
                        "name": "Vijaya Kunde",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "38",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000690",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    },
                "2223000431":
                    {
                        "name": "Viraj Joshikar",
                        "Branch": "Data Science",
                        "Year": "THIRD",
                        "Roll No": "1",
                        "Division": "A",
                        "Batch": "A-1",
                        "PRN": "2223000431",
                        "total_attendance": "0",
                        "last_attendance_time": "2024-04-28 00:54:34"
                    }
            }
        }
    }
}

# Add data to Firebase
for key, value in data.items():
    ref.child(key).set(value)

print("Data added successfully!")
