import boto3
# Open Management Console

aws_management_console=boto3.session.Session(profile_name='default')
# Open IAM Console

ec2_console=aws_management_console.client(service_name='ec2')

## stop instance
responce=ec2_console.stop_instances(
    InstanceIds=['i-0348a726ad727d760']
)
## start instance
responce=ec2_console.start_instances(
    InstanceIds=['i-0348a726ad727d760']
)
## Terminate instance
responce=ec2_console.terminate_instances(
    InstanceIds=['i-0348a726ad727d760']
)

# reboot instance

responce=ec2_console.reboot_instances(
    InstanceIds=['i-0348a726ad727d760']
)