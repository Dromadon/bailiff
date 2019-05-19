from bailiff.security_group import (
    parse_security_group,
    select_security_group,
    security_group_info)
from tests import sg
import pytest

def test_security_group_is_none_should_raise_exception():
  # Given
  expected_result = [(None, None, None)]
  
  # When
  with pytest.raises(ValueError) as e:
    security_group = parse_security_group(None)

  # Then
  assert 'Security Group is None' in str(e)


def test_parse_security_group_should_return_cidr_and_ports():
    # Given

    # When
    result = parse_security_group(sg.launch_wizard_52_with_ports)

    # Then
    assert result == [("86.212.165.166/32", 80, 443)]

def test_parse_security_group_should_return_ports_0_to_65535_when_ports_not_mentionned():
    # Given

    # When
    result = parse_security_group(sg.launch_wizard_52)

    # Then
    assert result == [("86.212.165.166/32", 0, 65535)]

def test_parse_security_group_should_return_all_cidrs():
    # Given

    # When
    result = parse_security_group(sg.launch_wizard_52_with_several_cidr)

    # Then
    assert result == [("86.212.165.166/32", 80, 443),
                        ("87.212.165.166/32", 80, 443)]

def test_select_security_group_should_return_subset_of_groups():
    # Given
    name = 'launch-wizard-52'
    # When
    result = select_security_group(sg.response, name)

    # Then
    assert result['GroupName'] == name

def test_security_group_info():
    # Given
    name = 'ClouderaAdministrator'

    # When
    result = security_group_info(sg.response, name)

    # Then
    assert result == [('84.167.119.54/32', 80, 80),
('84.167.119.54/32', 50070, 50070),
('84.167.119.54/32', 8888, 8888),
('84.167.119.54/32', 19888, 19888),
('84.167.119.54/32', 8042, 8042),
('172.31.0.0/16', 0, 65535),
('87.168.123.243/32', 0, 65535),
('84.167.119.54/32', 22, 22),
('84.167.119.54/32', 7180, 7180),
('84.167.119.54/32', 7183, 7183),
('84.167.119.54/32', 8088, 8088),
('84.167.119.54/32', 443, 443)]
