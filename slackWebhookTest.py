
from flask import Flask
import json
import datetime
import requests

app = Flask(__name__)

def getduration(td):
    return str(td.days) + ' days'

class exRetro:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class msg:
    def __init__(self, text):
        self.text = text

@app.route('/', methods=['POST'])
def freedom():
    exMembers = []
    exMembers.append(exRetro("MEMBER1", getduration(datetime.date.today() - datetime.date(2017, 9, 2))))
    exMembers.append(exRetro("MEMBER2", getduration(datetime.date.today() - datetime.date(2017, 11, 1))))
    exMembers.append(exRetro("MEMBER3", getduration(datetime.date.today() - datetime.date(2017, 12, 1))))

    result = "Congratulation on your freedom gentleman \n\n"
    for member in exMembers:
        result += member.name + ": " + member.duration + " \n"

    # Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
    webhook_url = '<some_webhook_url>'
    slack_data = json.dumps(msg(result).__dict__)

    response = requests.post(webhook_url, data=slack_data, headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


