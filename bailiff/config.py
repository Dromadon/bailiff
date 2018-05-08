import logging
import os

#We're making quite a simple script, so no need for uber-powered logging
logging.basicConfig(level=logging.INFO)

SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']

try:
    SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
except KeyError:
    SLACK_CHANNEL = 'test_garbage'

try:
    SLACK_INTRO_MESSAGE = os.environ['SLACK_INTRO_MESSAGE']
except KeyError:
    SLACK_INTRO_MESSAGE = 'Hello there, here are our EC2 instances '

try:
    SLEEPY_THRESHOLD = os.environ['SLEEPY_THRESHOLD']
except KeyError:
    SLEEPY_THRESHOLD = 15

#This we do not need as a var, but better extracted here than in the middle of the code
categories_headers = {
    'unnamed': {'Id': 'Id', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'},
    'untrigramed': {'Name': 'Name', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'},
    'sleepy': {'Trigram': 'Trigram', 'Name': 'Name', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'},
    'legit': {'Trigram': 'Trigram', 'Name': 'Name', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'}
}

REGIONS=['eu-west-1','eu-west-2', 'eu-central-1']