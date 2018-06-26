from slackclient import SlackClient
import os



class SlackWrapper:

    def __init__(self, slack_api_token, slack_channel, slack_intro_message):
        self.slack_client = SlackClient(slack_api_token)
        self.slack_channel = slack_channel
        self.slack_intro_message = slack_intro_message

    def post_to_slack(self, message):
        self.slack_client.api_call("chat.postMessage", channel=self.slack_channel, link_names=True, text=self.slack_intro_message+"@channel\n```"+message+"```")
