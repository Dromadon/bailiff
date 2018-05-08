import boto3
import bailiff.instance as bi
import bailiff.utils.instance as bu
from operator import itemgetter

import bailiff.slack
import bailiff.utils.printing as bp

unnamed_instances=[]
untrigramed_instances=[]
sleepy_instances=[]
legit_instances=[]

regions=['eu-west-1','eu-west-2', 'eu-central-1']

for region in regions:
  ec2 = boto3.client('ec2', region_name=region)
  response = ec2.describe_instances()
  for r in response['Reservations']:
    for i in r['Instances']:
      instance_information = bi.extract_instance_information(i)
      instance_information['Region'] = region
      lists = {
        'UNNAMED': unnamed_instances,
        'UNTRIGRAMMED': untrigramed_instances,
        'SLEEPY': sleepy_instances,
        None: legit_instances
      }
      state = bi.classify_instance(instance_information)
      lists[state].append(instance_information)

unnamed_instances.sort(key=itemgetter('LaunchDate'))
untrigramed_instances.sort(key=itemgetter('Name'))
sleepy_instances.sort(key=itemgetter('Trigram'))
legit_instances.sort(key=itemgetter('LastActionDate'))


instances_categories = [
  {'category_name': 'sans nom',
  'instances': unnamed_instances,
  'headers': {'Id': 'Id', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'}},
  {'category_name': 'sans trigramme',
  'instances': untrigramed_instances,
  'headers': {'Name': 'Name', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'}},
  {'category_name': 'endormies',
  'instances': sleepy_instances,
  'headers': {'Trigram': 'Trigram', 'Name': 'Name', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'}},
  {'category_name': 'légitimes',
  'instances': legit_instances,
  'headers': {'Trigram': 'Trigram', 'Name': 'Name', 'Launch date': 'LaunchDate', 'Last action date': 'LastActionDate', 'Region': 'Region'}},
]

message = bp.get_display_message(instances_categories)
print(message)

bailiff.slack.post_to_slack(message)