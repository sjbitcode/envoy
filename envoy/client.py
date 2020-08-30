import requests

from .models import User


class GithubClient:
    BASE_URL = 'https://api.github.com'

    def get_user(self, username):
        """
        Fetches the user github endpoint with username
        and returns a User object with attributes.
        """
        if not username:
            raise Exception('Username is not valid')

        user_endpoint = f'{self.BASE_URL}/users/{username}'
        response = requests.get(user_endpoint)
        response_json = response.json()

        if not response.ok:
            raise Exception(f'Bad response - {response_json["message"]}')

        return User(
            username,
            response_json.get('name'),
            response_json.get('html_url'),
            response_json.get('avatar_url'),
            response_json.get('public_repos'),
            response_json.get('followers'),
            response_json.get('following'),
            response_json.get('updated_at')
        )
