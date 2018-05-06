import re
import datetime

def print_instance(instance=None,):
  name = get_instance_name_from_tags(instance['Tags'])
  if name is None:
    name = instance['InstanceId']
  print(f'{name} : {str(get_instance_last_action_date(instance))}')
  return None

def get_instance_name_from_tags(tags={}):
  for t in tags:
    if t['Key']=='Name':
      return t['Value']
  return None

def get_instance_trigram(name=""):
  trigram_regex=re.compile('^([a-zA-Z]{3,4})[^a-zA-Z]{1}.*')
  match = trigram_regex.match(name)
  if match:
    return match.group(1)
  else:
    return None

def get_instance_last_action_date(instance=None):
  state_transition_date = get_instance_last_action_date_from_state_transition(instance['StateTransitionReason'])
  if state_transition_date:
      return state_transition_date
  else:
      return get_instance_launch_date(instance['LaunchTime'])

def get_instance_last_action_date_from_state_transition(status=""):
  date_regex=re.compile(".+\(([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} GMT)\)$")
  match=date_regex.match(status)
  if not match:
      return None
  
  date_string=match.group(1)
  return datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S GMT')

def get_instance_launch_date(launch_time=""):
  date_regex=re.compile("^([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}).[0-9]{3}Z$")
  match=date_regex.match(launch_time)
  if not match:
      return None
  
  date_string=match.group(1)
  return datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')

def is_instance_stopped(instance=None):
  code=instance['State']['Code']
  if code==80:
      return True
  else:
      return False
