import boto3
ec2 = boto3.resource('ec2')
instance_id = "i-011154c6c6da3d7da"
instance = ec2.Instance(instance_id)
instance.terminate()
