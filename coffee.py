import pandas as pd

df = pd.read_csv('/Users/sohilbhatia/Downloads/Swarms.csv')
df.drop(df.columns.difference(['X', 'Y', 'STARTDATE']), 1, inplace=True)
df.sort_values(by=['STARTDATE'], inplace=True, ascending=True)
df.to_csv("newSwarms.csv")

df = pd.read_csv('newSwarms.csv')
df.drop(df.columns.difference(['X', 'Y', 'STARTDATE']), 1, inplace=True)

df['Year'] = pd.DatetimeIndex(df['STARTDATE']).year
df['Month'] = pd.DatetimeIndex(df['STARTDATE']).month

avg_df = pd.DataFrame(columns=['Lat', 'Long', 'Year', 'Month'])

Month = df['Month'][0]
Year = df['Year'][0]

dataPoints = 0

totalLong = 0
totalLat = 0
index = 0

for i in range(df.shape[0]):
    if (i != 0 and dataPoints == 0):
        currentMonth = df['Month'][i - 1]
        currentYear = df['Year'][i - 1]
    else:
        currentMonth = df['Month'][i]
        currentYear = df['Year'][i]

    if (currentMonth == Month and currentYear == Year):
        dataPoints += 1
        totalLong += df['Y'][i]
        totalLat += df['X'][i]
    else:
        avg_df = avg_df.append(
            {'Long': (totalLong / dataPoints), 'Lat': (totalLat / dataPoints), 'Year': Year, 'Month': Month},
            ignore_index=True)

        Month = df['Month'][i]
        Year = df['Year'][i]
        totalLong = 0
        totalLat = 0
        dataPoints = 0

from math import radians, sin, cos, asin, sqrt

inputLat = df['X'][27181]
inputLong = df['Y'][27181]

realLat = -9.31166666699994
realLong = 15.736388889

minDistance = 10000
minIndex = 0
currentDistance = 0


def distance(long1, lat1, long2, lat2):
    distance = (((lat2 - lat1) ** 2) + ((long2 - long1) ** 2)) ** 0.5
    return distance


for i in range(avg_df.shape[0]):
    currentDistance = distance(inputLong, inputLat, avg_df['Long'][i], avg_df['Lat'][i])
    if ((currentDistance < minDistance) and currentDistance > 0.01):
        minDistance = currentDistance
        minIndex = i

# print(minDistance)
# print(minIndex)
print(str(avg_df["Lat"][minIndex + 1]) + " " + str(avg_df["Long"][minIndex + 1]))


# print(str(realLat) + " " + str(realLong))


def distanceMiles(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    return 2 * 3958.756 * asin(sqrt(a))

# print(distanceMiles(avg_df["Long"][minIndex+1], avg_df["Lat"][minIndex+1], realLong, realLat))

from firebase_admin import db

import firebase_admin

from firebase_admin import credentials

# Get a database reference to our blog.

cred = credentials.Certificate('/Users/sohilbhatia/Downloads/predictivemodel-63227-firebase-adminsdk-by0r7-06300b0d29.json')

# Initialize the app with a service account, granting admin privileges

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://predictivemodel-63227.firebaseio.com/'

})


ref = db.reference()

users_ref = ref.child('users')

users_ref.set({

    'pred': {

        'lat': float(avg_df["Lat"][minIndex + 1]),
        'long': float(avg_df["Long"][minIndex + 1])

    }

})

