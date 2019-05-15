import boto3


def lambda_handler(object, context):

    #List all regions in your account
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    #Print all regions to show up in CloudWatch logs
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Region:", region)

        #Find all EBS volumes that are unattached (available)
        volumes = ec2.volumes.filter(
            Filters=[{'Name': 'status', 'Values': ['available']}])

        #For loop to delete all unused volumes 
        for volume in volumes:
            v = ec2.Volume(volume.id)
            print("Deleting EBS volume: {}, Size: {} GiB".format(v.id, v.size))
            v.delete()
