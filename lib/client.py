from history import History

class Client():
    def __init__(self, id, name, email, history=History()):
        self.id = id
        self.name = name
        self._email = email
        self.history = history

    def is_loyal() -> bool:
        pass
