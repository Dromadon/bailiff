from bailiff.main import process_security_groups
from unittest.mock import patch,Mock, MagicMock

def test_process_security_groups_should_call_aws_api():
    patched_client = MagicMock()
    regions = ['eu-west-1']
    with patch('boto3.client', return_value=patched_client):
        process_security_groups(regions)
    patched_client.describe_security_groups.assert_called_once()