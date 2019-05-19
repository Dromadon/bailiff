launch_wizard_52_with_several_cidr = {
            "Description": "launch-wizard-52 created 2018-12-06T15:23:41.573+01:00",
            "GroupName": "launch-wizard-52",
            "IpPermissions": [
                {
                    "FromPort": 80,
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "86.212.165.166/32"
                        },
                        {
                            "CidrIp": "87.212.165.166/32"
                        }
                    ],
                    "ToPort": 443,
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "969076149354",
            "GroupId": "sg-0125dcc12581327fa",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "VpcId": "vpc-4736e923"
        }
launch_wizard_52_with_ports = {
            "Description": "launch-wizard-52 created 2018-12-06T15:23:41.573+01:00",
            "GroupName": "launch-wizard-52",
            "IpPermissions": [
                {
                    "FromPort": 80,
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "86.212.165.166/32"
                        }
                    ],
                    "ToPort": 443,
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "969076149354",
            "GroupId": "sg-0125dcc12581327fa",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "VpcId": "vpc-4736e923"
        }
        
launch_wizard_52 = {
            "Description": "launch-wizard-52 created 2018-12-06T15:23:41.573+01:00",
            "GroupName": "launch-wizard-52",
            "IpPermissions": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "86.212.165.166/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "969076149354",
            "GroupId": "sg-0125dcc12581327fa",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "VpcId": "vpc-4736e923"
        }

response = {
    "SecurityGroups": [
        {
            "Description": "ClouderaAdministrator",
            "GroupName": "ClouderaAdministrator",
            "IpPermissions": [
                {
                    "FromPort": 80,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 80,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 50070,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 50070,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 8888,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 8888,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 19888,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 19888,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 8042,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 8042,
                    "UserIdGroupPairs": []
                },
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "172.31.0.0/16"
                        },
                        {
                            "CidrIp": "87.168.123.243/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 22,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 22,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 7180,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 7180,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 7183,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 7183,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 8088,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 8088,
                    "UserIdGroupPairs": []
                },
                {
                    "FromPort": 443,
                    "IpProtocol": "tcp",
                    "IpRanges": [
                        {
                            "CidrIp": "84.167.119.54/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "ToPort": 443,
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "969076149354",
            "GroupId": "sg-0110b667",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "VpcId": "vpc-4736e923"
        },
        {
            "Description": "launch-wizard-52 created 2018-12-06T15:23:41.573+01:00",
            "GroupName": "launch-wizard-52",
            "IpPermissions": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "86.212.165.166/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "OwnerId": "969076149354",
            "GroupId": "sg-0125dcc12581327fa",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "VpcId": "vpc-4736e923"
        }
    ],
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="
}
