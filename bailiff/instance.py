import bailiff.utils.instance as utils
import datetime

def extract_instance_information(instance):
    information = {}
    information['Id'] = utils.get_instance_id(instance)
    information['Name'] = utils.get_instance_name_from_tags(instance['Tags'])
    information['Trigram'] = utils.get_instance_trigram(information['Name'])
    information['LastActionDate'] = utils.get_instance_last_action_date(instance)
    information['LaunchDate'] = instance['LaunchTime'].date()
    information['Stopped'] = utils.is_instance_stopped(instance)

    return information

def classify_instance(instance_information):
    if not instance_information['Name']:
        return 'UNNAMED'
    
    if not instance_information['Trigram']:
        return 'UNTRIGRAMMED'

    if instance_information['Stopped'] and datetime.date.today() - instance_information['LastActionDate'] > datetime.timedelta(15):
        return 'SLEEPY'

    return None