import bailiff.utils as bu
import datetime
import mock

class TestUtils:

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

    def test_get_instance_trigram_returns_none_if_no_trigram_exists(self):
        # Given
        name='workernode'
        # When
        trigram = bu.get_instance_trigram(name)
        # Then
        assert trigram==None

    def test_get_instance_last_action_date_from_state_transition_returns_a_correct_date(self):
        # Given
        state_message='User initiated (2016-06-23 23:39:15 GMT)'
        expected_date=datetime.datetime(2016, 6, 23, 23, 39, 15, tzinfo=None)
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

    def test_get_instance_launch_date_returns_a_correct_date(self):
        # Given
        launch_time='2017-04-19T13:47:05.000Z'
        expected_date=datetime.datetime(2017, 4, 19, 13, 47, 5, 0, tzinfo=None)
        # When
        launch_date = bu.get_instance_launch_date(launch_time)
        # Then
        assert launch_date==expected_date

    def test_get_instance_launch_date_returns_none_if_unset(self):
        # Given
        launch_time=''
        # When
        launch_date = bu.get_instance_launch_date(launch_time)
        # Then
        assert launch_date==None

    def test_is_instance_stopped_returns_true(self):
        # Given
        instance = {'State': {'Code':80, 'Name': 'Stopped'}}
        # When
        is_stopped = bu.is_instance_stopped(instance)
        # Then
        assert is_stopped==True