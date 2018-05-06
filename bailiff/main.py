import boto3
import bailiff.utils as bu

ec2 = boto3.client('ec2', region_name='eu-west-1')
response = ec2.describe_instances()

unnamed_instances=[]
untrigramed_instances=[]
sleepy_instances=[]
legit_instances=[]

for r in response['Reservations']:
  for i in r['Instances']:
    name = bu.get_instance_name_from_tags(i['Tags'])
    if name is None:
      unnamed_instances.append(i)
      break
    
    trigram = bu.get_instance_trigram(name)
    if trigram is None:
      untrigramed_instances.append(i)
      break

    

    legit_instances.append(i)


print('Unnamed instances:')
for i in unnamed_instances:
  bu.print_instance(i)
print('Untrigramed instances:')
for i in untrigramed_instances:
  bu.print_instance(i)
print('Legit instances:')
for i in legit_instances:
  bu.print_instance(i)