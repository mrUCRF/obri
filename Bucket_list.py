import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('test-bucket')

for i in bucket.objects.all():
    print(i.key)
