import boto3
import bailiff.instance as bi
import bailiff.utils.instance as bu
from operator import itemgetter

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
sleepy_instances.sort(key=itemgetter('LastActionDate'))
legit_instances.sort(key=itemgetter('LaunchDate'))

print('Unnamed instances:')
for i in unnamed_instances:
  bu.print_instance(i)
print('Untrigramed instances:')
for i in untrigramed_instances:
  bu.print_instance(i)
print('Sleepy instances:')
for i in sleepy_instances:
  bu.print_instance(i)
print('Legit instances:')
for i in legit_instances:
  bu.print_instance(i)