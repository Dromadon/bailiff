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
    assert result == [{"cidr": "86.212.165.166/32", "port_from": 80, "port_to": 443}]


def test_parse_security_group_should_return_ports_0_to_65535_when_ports_not_mentionned():
    # Given

    # When
    result = parse_security_group(sg.launch_wizard_52)

    # Then
    assert result == [{"cidr": "86.212.165.166/32", "port_from": 0, "port_to": 65535}]


def test_parse_security_group_should_return_all_cidrs():
    # Given

    # When
    result = parse_security_group(sg.launch_wizard_52_with_several_cidr)

    # Then
    assert result == [{"cidr": "86.212.165.166/32", "port_from": 80, "port_to": 443},
                      {"cidr": "87.212.165.166/32", "port_from": 80, "port_to": 443}]


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
    assert result == [{"cidr": '84.167.119.54/32', "port_from": 80, "port_to": 80},
                      {"cidr": '84.167.119.54/32', "port_from": 50070, "port_to": 50070},
                      {"cidr": '84.167.119.54/32', "port_from": 8888, "port_to": 8888},
                      {"cidr": '84.167.119.54/32', "port_from": 19888, "port_to": 19888},
                      {"cidr": '84.167.119.54/32', "port_from": 8042, "port_to": 8042},
                      {"cidr": '172.31.0.0/16', "port_from": 0, "port_to": 65535},
                      {"cidr": '87.168.123.243/32', "port_from": 0, "port_to": 65535},
                      {"cidr": '84.167.119.54/32', "port_from": 22, "port_to": 22},
                      {"cidr": '84.167.119.54/32', "port_from": 7180, "port_to": 7180},
                      {"cidr": '84.167.119.54/32', "port_from": 7183, "port_to": 7183},
                      {"cidr": '84.167.119.54/32', "port_from": 8088, "port_to": 8088},
                      {"cidr": '84.167.119.54/32', "port_from": 443, "port_to": 443}]
