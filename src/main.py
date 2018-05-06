import boto3

ec2 = boto3.client('ec2', region_name='eu-west-1')
response = ec2.describe_instances()

def print_instance(instance=None):
  name = get_instance_name(instance['Tags'])
  if name is None:
    name = instance['InstanceId']
  print(f'{name}')
  return None

def get_instance_name(tags={}):
  for t in tags:
    if t['Key']=='Name':
      return t['Value']
  return None

for r in response['Reservations']:
  for i in r['Instances']:
    print_instance(i)


