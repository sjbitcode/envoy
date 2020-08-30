from envoy.client import GithubClient


if __name__ == '__main__':
    client = GithubClient()
    user = client.get_user('tunedmystic')
    print(user)
