"""
Usage: python -m unittest -v
"""
from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, MagicMock

from envoy.client import GithubClient


class TestGithubClient(TestCase):
    @patch('envoy.client.requests')
    def test__get_user__success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'name': 'Alice',
            'html_url': 'https://github.com/aliceCodes',
            'avatar_url': 'https://github.com/avatar/aliceCodes.jpg',
            'public_repos': 20,
            'followers': 25,
            'following': 50,
            'updated_at': '2020-01-12T01:14:59Z'
        }
        mock_response.ok = True

        mock_requests.get.return_value = mock_response
        user = GithubClient().get_user('aliceCodes')

        self.assertEqual(user.username, 'aliceCodes')
        self.assertEqual(user.name, 'Alice')
        self.assertEqual(user.url, 'https://github.com/aliceCodes')
        self.assertEqual(user.avatar_url, 'https://github.com/avatar/aliceCodes.jpg')
        self.assertEqual(user.repos, 20)
        self.assertEqual(user.followers, 25)
        self.assertEqual(user.following, 50)
        self.assertEqual(
            user.updated_at,
            datetime(2020, 1, 12, 1, 14, 59)
        )

    def test__get_user__no_username(self):
        with self.assertRaises(Exception) as e:
            GithubClient().get_user(None)

        self.assertEqual(str(e.exception), 'Username is not valid')

    @patch('envoy.client.requests')
    def test__get_user__bad_response(self, mock_requests):
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.json.return_value = {
            'message': 'some error...'
        }

        mock_requests.get.return_value = mock_response

        with self.assertRaises(Exception) as e:
            GithubClient().get_user('aliceCodes')

        self.assertEqual(str(e.exception), 'Bad response - some error...')