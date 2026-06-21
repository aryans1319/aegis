class LogNotFoundException(Exception):

    def __init__(self):
        super().__init__("Log not found")