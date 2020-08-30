from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class User:
    """ This class represents a Github user. """
    username: str
    name: str
    url: str
    avatar_url: str
    repos: int
    followers: int
    following: int
    updated_at_raw: datetime
    updated_at: str = field(init=False)

    def __post_init__(self):
        self.updated_at = datetime.strptime(
            self.updated_at_raw,
            '%Y-%m-%dT%H:%M:%SZ'
        )

    def __str__(self):
        return f'User <{self.username}>'

    @property
    def is_popular(self):
        return self.followers > 20

    @property
    def is_active(self):
        return self.updated_at >= datetime.now() - timedelta(days=7)
