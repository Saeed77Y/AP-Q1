class User:
    def __init__(self, username) -> None:
        self.username = username
        self.counter()

    user_count = 0

    @classmethod
    def counter(cls):
        cls.user_count += 1