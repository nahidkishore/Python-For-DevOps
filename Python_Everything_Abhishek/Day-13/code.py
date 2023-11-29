import boto3

client = boto3.client('s3')

# response = client.create_bucket(
#     Bucket='nahid-demo-bucket-boto3-123',
# )

response = client.get_bucket_acl(
    Bucket='nahid-demo-bucket-boto3-123',
   
)

print(response)