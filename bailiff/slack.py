from slackclient import SlackClient
import os
import config

sc = SlackClient(config.SLACK_API_TOKEN)

def post_to_slack(message):
    sc.api_call("chat.postMessage", channel=config.SLACK_CHANNEL, link_names=True, text=config.SLACK_INTRO_MESSAGE+"@channel\n```"+message+"```")
