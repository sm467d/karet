import json
from datetime import datetime
from twilio.rest import Client
import time

# Your Account SID from twilio.com/console
account_sid = "SID"
# Your Auth Token from twilio.com/console
auth_token  = "TKN"

client = Client(account_sid, auth_token)


def get_body(event): # takes in an event object
    '''
    Types:
        shower
        conjunction: two objects are close together in the sky
        perihilion: when object is closest to Sun
        apogee: moon furthest
        perigee: moon closest
        aphelion: object is furthest from the Sun
        equinox: date twice a year when the sun crosses the equator and day and night are the same length
        moon
        solstice
    '''
    body = ""
    match event["type"]:
        case "shower":
            body = "Be on the lookout for the " + event["name"] +  " meteor shower today! Visible from " + event["time"] + "!" 
        case "conjunction":
            body = "Conjunction today! Look up at " + event["time"] + " to see the " + event["name"] + " conjunction!"
        case "perihilion":
            body = "Earth's Perihelion is today, where the Earth is closest to the Sun. Don't look up, but expect a beautiful sunrise & sunset!"
        case "perigee":
            body = "Today, be on the lookout for a lunar perigee, when the moon is closest to the Earth. Have a bright night!"
        case "apogee":
            body = "Today, be on the lookout for a lunar apogee, when the moon is furthest to the Earth! "
        case "aphelion":
            body = "Earth's Aphelion is today, where the Earth is furthest from the Sun! Expect a beautiful sunrise and sunset!"
        case "equinox":
            if "Autumn" in event["name"]:
                body = "Today is the Autumnal Equinox, when the sun crosses the celestial equator in a southernly direction! Hope you're getting ready for Fall!"
            elif "Fall" in event["name"]:
                body = "Today is the Autumn Solstice! Have a great Fall!"
            elif event["name"] == "First Day of Spring":
                body = "Today is the Spring Solstice! Have a great Spring!"
            else: # Spring
                body = "Today is the Spring Equinox, when the sun crosses the celestial equator in a northern direction! Have a great Spring!"
        case "moon":
            body = "Moon Event today! Be on the look out for a " + event["name"] + " around " + event["peak"] + "!"
        case "solstice":
            if "Summer" in event["name"]:
                body = "Today is the Summer Solstice! Have a great Summer!"
            else:
                body = "Today is the Winter Solstice! Stay warm this Winter!"
        case "solar-eclipse":
            body = "Be on the lookout for a Partial Solar Eclipse today! Visible from " + event["peak"] +"!"
    return body


# Load events from JSON file
with open("test.json", "r") as f:
    events = json.load(f)
while True:
    # Get current date and time
    now = datetime.now()
    current_date = now.strftime("%m/%d/%Y")
    current_time = now.strftime("%I:%M:%S %p")
 
    # Iterate through events
    matching_event = None
    for event in events:
        if event["peak"] == current_date and event["time"] == current_time:
            matching_event = event 

    # Create message body
    if matching_event:
        message_body = get_body(matching_event)
        
            
    else:
        continue

    nums = ["TWILIO DB IMPORT"]
    for x in nums:
        message = client.messages.create(
            to= x, 
            from_="+12028665516",
            body= message_body)

        print(message.sid)
        
    time.sleep(60)
    
