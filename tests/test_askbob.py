
from bailiff.askbob import AskbobWrapper
import requests
import pytest

class TestAskbob:

    @pytest.fixture
    def askbob_wrapper(self, monkeypatch):
        monkeypatch.setattr('requests.post', mock_requests)
        monkeypatch.setattr('requests.get', mock_requests)
        return AskbobWrapper("dummy_id", "dummy_secret")

    @pytest.fixture
    def askbob_wrapper_exception(self, monkeypatch):
        monkeypatch.setattr('requests.post', mock_requests)
        aw = AskbobWrapper("dummy_id", "dummy_secret")
        monkeypatch.setattr('requests.post', mock_requests_exception)
        monkeypatch.setattr('requests.get', mock_requests_exception)
        return aw
    
    def test_get_email_from_people_data_returns_both_emails(self, askbob_wrapper):
        # Given
        trigrams=['AGR','ALB']
        people_data = [
            {'trigram': 'AGR', 'email': 'agr-test@octo.com'},
            {'trigram': 'ALB', 'email': 'alb-test@octo.com'}
        ]
        # When
        emails = askbob_wrapper._get_people_emails(trigrams=trigrams, people_data=people_data)
        # Then
        assert emails == {'AGR': ['agr@octo.com', 'agr-test@octo.com'], 'ALB': ['alb@octo.com', 'alb-test@octo.com']}

    def test_get_team_id_returns_id_if_correct_json(self, askbob_wrapper):
        # Given
        team_name = 'BDA'
        # When
        id = askbob_wrapper._get_team_id(team_name=team_name)
        # Then
        assert id == 1

    def test_get_team_id_returns_none_if_name_not_in_json(self, askbob_wrapper):
        # Given
        team_name = 'FAKE'
        # When
        id = askbob_wrapper._get_team_id(team_name=team_name)
        # Then
        assert id == None

    """def test_get_team_id_returns_none_if_teams_are_none(self, askbob_wrapper):
        # Given
        team_name = 'BDA'
        # When
        id = askbob_wrapper._get_team_id(team_name=team_name)
        # Then
        assert id == None"""

    def test_get_team_people_returns_none_if_team_is_none(self, askbob_wrapper_exception):
        # Given
        team_id = 1
        # When
        people = askbob_wrapper_exception._get_team_people(team_id=team_id)
        # Then
        assert people == None

    def test_get_team_people_returns_none_if_exception_occurs(self, askbob_wrapper_exception):
        # Given

        # When
        teams = askbob_wrapper_exception._get_teams()
        # Then
        assert teams == None

    def test_get_teams_returns_none_if_exception_occurs(self, askbob_wrapper_exception):
        # Given

        # When
        teams = askbob_wrapper_exception._get_teams()
        # Then
        assert teams == None

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