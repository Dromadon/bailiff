import bailiff.utils.instance as utils
import datetime
import logging
import bailiff.config

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
        logging.debug('Instance has been classified UNNAMED')
        return 'UNNAMED'
    
    if not instance_information['Trigram']:
        logging.debug('Instance has been classified Untrigrammed')
        return 'UNTRIGRAMMED'

    if instance_information['Stopped'] and datetime.date.today() - instance_information['LastActionDate'] > datetime.timedelta(15):
        logging.debug('Instance has been classified Sleepy')
        return 'SLEEPY'

    logging.debug('Instance has been classified Legit')
    return None
