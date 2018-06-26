import boto3

def main():
    ec2 = boto3.client('ec2', region_name='eu-west-1')
    print(ec2.describe_instances())
    print("coucou !")


if __name__==__main__:
    main()
