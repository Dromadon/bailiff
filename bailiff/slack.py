from slackclient import SlackClient
import os

slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)

def post_to_slack(message):
    sc.api_call("chat.postMessage", channel="test_garbage", link_names=True, text="Wesh @channel \n```"+message+"```")
