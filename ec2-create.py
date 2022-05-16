import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(ImageId='ami-0bd6906508e74f692', MinCount=1, MaxCount=1,
        InstanceType='t2.micro',
        Placement={'AvailabilityZone': 'ap-southeast-1a'},
        )
print(instance[0])
