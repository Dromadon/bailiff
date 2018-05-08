import boto3
from operator import itemgetter
import bailiff.instance as bi
import bailiff.utils.instance as bu
import bailiff.slack
import bailiff.utils.printing as bp
import logging

import bailiff.config as cf


unnamed_instances=[]
untrigramed_instances=[]
sleepy_instances=[]
legit_instances=[]

regions=cf.REGIONS

for region in regions:
  logging.info(f'Working on region {region}')
  ec2 = boto3.client('ec2', region_name=region)
  response = ec2.describe_instances()
  for r in response['Reservations']:
    for i in r['Instances']:
      logging.info(f'Analyzing instance {i["InstanceId"]}')
      instance_information = bi.extract_instance_information(i)
      instance_information['Region'] = region
      lists = {
        'UNNAMED': unnamed_instances,
        'UNTRIGRAMMED': untrigramed_instances,
        'SLEEPY': sleepy_instances,
        None: legit_instances
      }
      logging.debug(f'Classifying instance')
      state = bi.classify_instance(instance_information)
      lists[state].append(instance_information)

logging.info('Sorting instances lists')
unnamed_instances.sort(key=itemgetter('LaunchDate'))
untrigramed_instances.sort(key=itemgetter('Name'))
sleepy_instances.sort(key=itemgetter('Trigram'))
legit_instances.sort(key=itemgetter('LastActionDate'))


instances_categories = [
  {'category_name': 'sans nom',
  'instances': unnamed_instances,
  'headers': cf.categories_headers['unnamed']},
  {'category_name': 'sans trigramme',
  'instances': untrigramed_instances,
  'headers': cf.categories_headers['untrigramed']},
  {'category_name': 'endormies',
  'instances': sleepy_instances,
  'headers': cf.categories_headers['sleepy']},
  {'category_name': 'légitimes',
  'instances': legit_instances,
  'headers': cf.categories_headers['legit']},
]

logging.info('Displaying results')
message = bp.get_display_message(instances_categories)
print(message)

bailiff.slack.post_to_slack(message)