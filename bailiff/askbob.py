import requests as rq
import config as cf
import logging

class AskbobWrapper():

    def __init__(self, askbob_client_id, askbob_client_secret):
        params = {
            'grant_type': 'client_credentials',
            'client_id': askbob_client_id,
            'client_secret': askbob_client_secret
        }
        r = rq.post('https://askbob.octo.com/oauth/token', data=params)
        self.access_token = r.json()['access_token']

    def _get_teams(self):
        try:
            r = rq.get('https://askbob.octo.com/api/v2/teams', params={'access_token': self.access_token})
            return r.json()['data']
        except Exception as e:
            logging.error(e)
            logging.error("Resuming without Askbob teams")
            return None

    def _get_team_people(self, team_id=""):
        if team_id:
            try:
                r = rq.get(f'https://askbob.octo.com/api/v2/teams/{team_id}/people', params={'access_token': self.access_token})
                return r.json()['data']
            except Exception as e:
                logging.error(e)
                logging.error(f"Resuming without askbob people from team {team_id}")
                return None
        else: 
            return None
    
    def _get_team_id(self, team_name=""):
        teams = self._get_teams()
        for t in teams:
            if t['code_name'] == team_name:
                return t['id']
        return None

    def _get_people_emails(self, trigrams=[], people_data=[]):
        people_emails = {t: [f'{t}@octo.com'.lower()] for t in trigrams}
        for t in trigrams:
            for p in people_data:
                if p['trigram'] == t:
                    people_emails[t].append(p['email'])
                    break
        return people_emails

    def get_emails_from_trigram(self, team_name="", trigrams=[]):
        team_id = self._get_team_id(team_name)
        people_data = self._get_team_people(team_id)
        return self._get_people_emails(trigrams, people_data)

aw = AskbobWrapper(cf.ASKBOB_ID, cf.ASKBOB_SECRET)
emails = aw.get_emails_from_trigram(team_name="BDA", trigrams=['AGR', 'ALB'])
print(emails)
