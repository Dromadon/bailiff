import bailiff.utils.instance as bu
import datetime


class TestUtilsInstance:

    def test_get_instance_name_from_tags_returns_name_if_exists(self):
        # Given
        tags=[{'Key': 'Name', 'Value': 'MyName'}]
        # When
        name = bu.get_instance_name_from_tags(tags)
        # Then
        assert name=='MyName'

    def test_get_instance_name_from_tags_returns_none_if_no_name_exists(self):
        # Given
        tags=[{'Key': 'RandomTag', 'Value': 'RandomValue'}]
        # When
        name = bu.get_instance_name_from_tags(tags)
        # Then
        assert name==None

    def test_get_instance_trigram_returns_trigram_if_trigram_exists(self):
        # Given
        name_tri='AGR-test'
        name_quadri='PADE-test'
        # When
        trigram = bu.get_instance_trigram(name_tri)
        quadrigram = bu.get_instance_trigram(name_quadri)
        # Then
        assert trigram=='AGR'
        assert quadrigram=='PADE'

    def test_get_instance_trigram_returns_uppercase_trigram(self):
        # Given
        name='agr-test'
        # When
        trigram = bu.get_instance_trigram(name)
        # Then
        assert trigram=='AGR'

    def test_get_instance_trigram_returns_none_if_no_trigram_exists(self):
        # Given
        name='workernode'
        # When
        trigram = bu.get_instance_trigram(name)
        # Then
        assert trigram==None

    def test_get_instance_trigram_returns_none_if_name_is_none(self):
        # Given
        name=None
        # When
        trigram = bu.get_instance_trigram(name)
        # Then
        assert trigram==None

    def test_get_instance_last_action_date_from_state_transition_returns_a_correct_date(self):
        # Given
        state_message='User initiated (2016-06-23 23:39:15 GMT)'
        expected_date=datetime.date(2016, 6, 23)
        # When
        state_date = bu.get_instance_last_action_date_from_state_transition(state_message)
        # Then
        assert state_date==expected_date

    def test_get_instance_last_action_date_from_state_transition_returns_none_if_unset(self):
        # Given
        state_message=''
        # When
        state_date = bu.get_instance_last_action_date_from_state_transition(state_message)
        # Then
        assert state_date==None

    def test_is_instance_stopped_returns_true(self):
        # Given
        instance = {'State': {'Code':80, 'Name': 'Stopped'}}
        # When
        is_stopped = bu.is_instance_stopped(instance)
        # Then
        assert is_stopped==True

    def test_get_instance_id_returns_correct_id(self):
        # Given
        instance = {'InstanceId': 'i-018ee3a3e5cbc0472'}
        # When
        id = bu.get_instance_id(instance)
        # Then
        assert id=='i-018ee3a3e5cbc0472'