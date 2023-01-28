import json
from datetime import datetime
from twilio.rest import Client
import time

# Your Account SID from twilio.com/console
account_sid = "AC6990facbe1abd06e9bb3598d1cace632"
# Your Auth Token from twilio.com/console
auth_token  = "8f2fd1726259c77f187f6fa31751ad07"

client = Client(account_sid, auth_token)

# Load events from JSON file
with open("events.json", "r") as f:
    events = json.load(f)
while True:
    # Get current date and time
    now = datetime.now()
    current_date = now.strftime("%m/%d/%Y")
    current_time = now.strftime("%I:%M:%S %p")

    # Iterate through events
    matching_events = []
    for event in events:
        if event["peak"] == current_date and event["time"] == current_time:
            matching_events.append(event["name"])

    # Create message body
    if matching_events:
        message_body = "Today's events: " + ", ".join(matching_events)
    else:
        continue

    nums = ["+14432516117", "+12403748332", "+14438582675"]
    for x in nums:
        message = client.messages.create(
            to= x, 
            from_="+12028665516",
            body= message_body)

        print(message.sid)
    time.sleep(60)
