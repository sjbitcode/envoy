"""
Usage: python -m unittest -v
"""
from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import patch

from envoy.models import User


class TestUserModel(TestCase):
    def test__post_init__parses_datetime_correctly(self):
        user = User('', '', '', '', 0, 0, 0, '2020-01-12T01:14:59Z')
        expected_updated_at = datetime(2020, 1, 12, 1, 14, 59)
        self.assertEqual(user.updated_at, expected_updated_at)

    def test__str(self):
        user = User('aliceCodes', '', '', '', 0, 0, 0, '2020-01-12T01:14:59Z')
        self.assertEqual(user.__str__(), 'User <aliceCodes>')

    def test__is_popular(self):
        user = User('aliceCodes', '', '', '', 0, 25, 0, '2020-01-12T01:14:59Z')
        self.assertTrue(user.is_popular)

    @patch('envoy.models.datetime')
    def test__is_active(self, mock_datetime):
        mock_datetime.strptime = datetime.strptime
        mock_datetime.timedelta = timedelta
        mock_datetime.now.return_value = datetime(2020, 1, 15, 0, 0, 0)

        user = User('aliceCodes', '', '', '', 25, 0, 0, '2020-01-12T01:14:59Z')
        self.assertTrue(user.is_active)

    @patch('envoy.models.datetime')
    def test__is_not_active(self, mock_datetime):
        mock_datetime.strptime = datetime.strptime
        mock_datetime.timedelta = timedelta
        mock_datetime.now.return_value = datetime(2020, 1, 20, 0, 0, 0)

        user = User('aliceCodes', '', '', '', 25, 0, 0, '2020-01-12T01:14:59Z')
        self.assertFalse(user.is_active)
