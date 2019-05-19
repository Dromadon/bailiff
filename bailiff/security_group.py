def parse_security_group(security_group):
    if not security_group:
        raise ValueError('Security Group is None')
    result = []
    for i_p in security_group.get('IpPermissions'):
        from_port = i_p.get('FromPort', 0)
        to_port = i_p.get('ToPort', 65535)
        for c in i_p.get('IpRanges'):
            result.append((c.get('CidrIp'), from_port, to_port))
    return result


def select_security_group(raw_json, name):
    security_groups = raw_json['SecurityGroups']
    for sg in security_groups:
        if sg.get('GroupName') == name:
            return sg
    return None

def security_group_info(raw_json, name):
    sg = select_security_group(raw_json, name)
    return parse_security_group(sg)