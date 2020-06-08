from firebase_admin import db

import firebase_admin

from firebase_admin import credentials
import requests


URL = "https://locustlocater-e46b6.firebaseio.com/.json"

r = requests.get(url=URL)

dataNext = r.json()

cred = credentials.Certificate('/Users/sohilbhatia/Downloads/predictivemodel-63227-firebase-adminsdk-by0r7-06300b0d29.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://predictivemodel-63227.firebaseio.com/'
})
ref = db.reference()

data = ref.get()


from math import radians, sin, cos, asin, sqrt

def distanceMiles(lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    return 2 * 3958.756 * asin(sqrt(a))


predictedLong = (data['users']['pred']['long'])
predictedLat = (data['users']['pred']['lat'])
userLong = (dataNext['Longitude'])
userLat = (dataNext['Latitude'])
userPhoneNumber = "+1" + str(dataNext['Phone Number'])
name = (dataNext['Name'])

from twilio.rest import Client

account_sid = 'ACc868f3ad31a58de95be97de8d7e22ed0'
auth_token = '232c21a5ab59a983dfa4e1cb7ebc67ca'
client = Client(account_sid, auth_token)


message = client.messages.create(
    from_='+14803866032',
    body="Hello " + name + "." + " You are currently " + str(round(distanceMiles(predictedLong, predictedLat, userLong, userLat), 0)) + " miles from the next predicted locust swarm. You will be notified when it is 450 miles from your location.",
    to="+14257771133"
)



print(message.sid)

#"Hello " + name + "." + "You are " + str(distanceMiles(predictedLong, predictedLat, userLong, userLat)) + " miles from the next predicted locust swarm. You will be notified with further updates.",
print(distanceMiles(predictedLong, predictedLat, userLong, userLat))
