import boto3

# Open Management Console

aws_management_console=boto3.session.Session(profile_name='default')
# Open IAM Console

ec2_console=aws_management_console.client(service_name='ec2')
# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
#result=ec2_console.describe_instances()['Reservations']

# getting all running instances
def get_running_instances():
    reservations = ec2_console.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
        
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
            
get_running_instances()