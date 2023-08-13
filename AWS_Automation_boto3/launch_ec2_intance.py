import boto3
# Open Management Console

aws_management_console=boto3.session.Session(profile_name='default')
# Open IAM Console

ec2_console=aws_management_console.client(service_name='ec2')

responce=ec2_console.run_instances(
  ImageId='ami-053b0d53c279acc90',  # Replace with the desired AMI ID
    InstanceType= 't2.micro',
    KeyName= 'test-key',       # Replace with your key pair name
    MinCount= 1,
    MaxCount= 1
)