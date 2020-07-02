from datetime import datetime
from dateutil import parser as date_parser
import requests
import kaggle
import json

########################################################################################
# Configuration:
########################################################################################
#
# url for slack bot
# ex. 
#   URL = 'https://hooks.slack.com/services/123456789'
URL = ''
#
#
# target competition
# ex.
#   COMPETITION = 'm5-forecasting-accuracy'
COMPETITION = ''
########################################################################################


def get_messages():
    data = []
    submissions = kaggle.api.competitions_submissions_list(COMPETITION)
    for s in submissions:
        pub_score = float(s['publicScore']) if s['publicScore'] is not None else 99
        pri_score = float(s['privateScore']) if s['privateScore'] is not None else 99
        data.append({
            'date': date_parser.parse(s['date']),
            'date_str': date_parser.parse(s['date']).strftime('%Y-%m-%d'),
            'public_score': pub_score,
            'private_score': pri_score,
            'submitted_by': s['submittedBy'],
            'url': s['url']
        })
    message_data = sorted(data, key=lambda x: x['date'], reverse=True)

    best_score = min(d['public_score'] for d in data)
    for d in data:
        if d['public_score'] == best_score:
            best_score = d

    return message_data, best_score


def post_newest_submissions():
    message_data, best_score = get_messages()
    msgs = ['Public Score: {:.5f}     by {:10} ({})'.format(d['public_score'], d['submitted_by'], d['date_str']) for d in message_data[:5]]
    attachments = []
    for msg in msgs:
        attachments.append({
            'fallback': 'Newest Submissions!',
            'color': 'good',
            'text': msg
        })
    data = {
        'text': 'Newest Submssions！',
        'attachments': attachments
    }
    res = requests.post(URL, json=data, headers={'Content-Type': 'application/json'})


def post_best_score():
    message_data, best_score = get_messages()
    data = {
        'text': 'Current Best Score!',
        'attachments': [{
            'fallback': 'Current Best Score!',
            'color': 'good',
            'text': 'Public Score: {:.5f}     by {:10} ({})'.format(best_score['public_score'], best_score['submitted_by'], best_score['date_str'])
        }]
    }
    res = requests.post(URL, json=data, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':

    post_best_score()
    post_newest_submissions()
