import boto3
iam_console_resource=boto3.resource('iam')

for each_user in iam_console_resource.users.all():
  #print(each_user)
  print(each_user.name)

