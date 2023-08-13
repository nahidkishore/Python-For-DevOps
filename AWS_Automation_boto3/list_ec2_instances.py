import boto3
from pprint import pprint
# Open Management Console

aws_management_console=boto3.session.Session(profile_name='default')
# Open IAM Console

ec2_console=aws_management_console.client(service_name='ec2')
# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
result=ec2_console.describe_instances()['Reservations']
#print(result)

for each_instance in result:
  for value in each_instance['Instances']:
    print(value['InstanceId'])