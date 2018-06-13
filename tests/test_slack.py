
from bailiff.slack import SlackWrapper
import requests
import pytest
import pytest_mock
from slackclient import SlackClient

class TestSlack:

    @pytest.fixture
    def slack_wrapper(self, mocker, monkeypatch):
        sw = SlackWrapper("dummy_token", "dummy_channel", "dummy_message")
        return sw
    
    def test_post_to_slack_triggers_api_call(self, slack_wrapper, mocker):
        # Given
        mocker.spy(slack_wrapper.slack_client, 'api_call')
        # When
        slack_wrapper.post_to_slack("test")
        # Then
        assert slack_wrapper.slack_client.api_call.call_count == 1

def mock_requests(*args, **kwargs):
    if args[0] == 'https://askbob.octo.com/oauth/token':
        return MockResponse({'access_token': 'dummyvalue'})
    elif args[0] == 'https://askbob.octo.com/api/v2/teams':
        return MockResponse({'data': [
            {'id': 1, 'code_name': 'BDA'},
            {'id': 2, 'code_name': 'SCALE'}
        ]})
    elif args[0] == 'https://askbob.octo.com/api/v2/teams/1/people':
        return MockResponse({'data':[
            {'trigram': 'AGR', 'email': 'agr-test@octo.com'},
            {'trigram': 'ALB', 'email': 'alb-test@octo.com'}
        ]})

def mock_requests_exception(*args, **kwargs):
    raise requests.RequestException()

    

class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data