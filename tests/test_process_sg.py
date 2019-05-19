from bailiff.main import process_security_groups
from unittest.mock import patch, Mock, MagicMock


def test_process_security_groups_should_call_aws_api():
    patched_client = MagicMock()
    regions = ['eu-west-1']
    with patch('boto3.client', return_value=patched_client):
        process_security_groups(regions)
    patched_client.describe_security_groups.assert_called_once()


def test_process_security_groups_should_return_a_dict():
    patched_client = MagicMock()
    regions = ['eu-west-1']
    with patch('boto3.client', return_value=patched_client):
        security_groups = process_security_groups(regions)
    assert isinstance(security_groups, dict)


def test_process_security_groups_should_return_a_dict_with_regions_as_key():
    patched_client = MagicMock()
    regions = ['eu-west-1', 'eu-west-2']
    with patch('boto3.client', return_value=patched_client):
        security_groups = process_security_groups(regions)
    assert list(security_groups.keys()) == regions


def test_process_security_groups_should_return_sg_info():
    patched_client = MagicMock()
    patched_sg = MagicMock()
    patched_sg.return_value = ["SG information1", "SG information2"]
    regions = ['eu-west-1', 'eu-west-2']
    with patch('boto3.client', return_value=patched_client):
        with patch('bailiff.security_group.security_group_info', return_value=["SG information1", "SG information2"], ):
            security_groups = process_security_groups(regions)
    assert security_groups[regions[0]] == "SG information1"
