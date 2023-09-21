class BaseException(Exception):
    """Base class for all FEMEM exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message