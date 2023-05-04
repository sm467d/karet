# Karet - Astronomy for All

See our HoyaHacks2023 Submission! https://youtu.be/x57r54HSsVU

Karet is an application designed to make astronomy accessible to people of all levels of interest. It provides scheduled notifications for celestial events such as meteor showers, eclipses, and constellations. Karet aggregates data from 5 astronomical APIs to create a comprehensive database of event notifications. It also integrates "Galileo", a generative transformer model fine-tuned on celestial data sets to provide insights into all things astronomy via SMS.

## Inspiration

During the first night of Hoya Hacks, the Astronomy Club offered to show the Orion Nebula, and the team felt that everyone should have access to the ability to see shooting stars, eclipses, and constellations. With backgrounds in physics and astrophysics, the team decided to create something easy and accessible to the average Earthling, doing all the hard work and research so you don't have to.

## What it does

Karet has two main functionalities:

1. Aggregates data from 5 astronomical APIs to create a scheduled database of event notifications, with peak times (the best time to look up) for events such as meteor showers, based on Earth's axis, rotation, Georgetown's geographical location, and particular celestial event radiants. For events with wider ranges, the Karet SMS service (powered by Twilio) sends an alert to be on the lookout throughout the day, but for events with more consistent ecliptics, the Karet SMS service is able to send messages just minutes before the event, telling the user to simply, "look up" and view the amazing work of our universe!
2. Integrates "Galileo", a generative transformer model fine-tuned on celestial data sets, events, and pre-trained astronomical ecliptic calculations, to provide insights into all things astronomy. In short, a somewhat smart AI chatbot accessible via SMS.

## How we built it

The team created a site that takes in a user's phone number and appends it to a Firestore database. Then they combined and cleaned data from several APIs to train the model. After that, they created a script that's always running, iterating through the "Events" database each minute, checking for events that match the current date and time. When they do, it sends tailored messages to the users in the Firestore database.

For the SMS service bot, the team fine-tuned a model using the OpenAI API endpoints and integrated the "Completion" endpoint in the Twilio console, so that it is always awaiting a message and ready to help!

The team also built the site using React, and got their domain name (karet.space) from domain.com.


## Accomplishments that we're proud of

The team achieved several accomplishments, including:

- Accurate ecliptic calculations using IMO web-scraping of celestial event trajectories.
- Model integration: Successfully training a GPT3 model on hundreds of datapoints and parameters,
