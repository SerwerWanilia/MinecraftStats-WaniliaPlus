import json
import datetime
import random as rnd
import os

def dailyEvents(statByName):
    startDay = datetime.datetime.now() + datetime.timedelta(days=1)
    endDay = datetime.datetime.now() + datetime.timedelta(days=2)
    startTime = startDay.strftime("%Y-%m-%d 00:00")
    endTime = endDay.strftime("%Y-%m-%d 00:00")

    events = []
    newEvent = 0

    if os.path.exists('./dailyevents.json'):
        with open('dailyevents.json', 'r') as jsonfile:
            events = json.load(jsonfile)

    eventsCount = len(events)
    if not eventsCount or events[-1]['startTime'] != startTime:
        eventNumber = eventsCount + 1
        randomStat = rnd.choice(list(statByName.keys()))
        event = {
            'name': f'daily_event_{eventNumber}',
            'title': f'Codzienny event #{eventNumber}',
            'stat': randomStat,
            'startTime': startTime,
            'endTime': endTime
        }
        events.append(event)
        newEvent = 1

    if newEvent:
        with open('dailyevents.json', 'w') as jsonfile:
            jsonfile.write(json.dumps(events, indent=4))

    return events