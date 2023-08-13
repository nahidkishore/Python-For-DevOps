import boto3
s3= boto3.resource('s3')
ec2= boto3.resource('ec2')
print(s3.buckets.all())
for buckets in s3.buckets.all():
  print(buckets)
for buckets in s3.buckets.all():
  print(buckets.name)  


c=0
for buckets in s3.buckets.all():
  print(buckets)
  c=c+1

s3.Bucket("test-bucket-python-devops").download_file("dev.png","dev.png")  