class IncidentNotFoundException(Exception):
    def __init__(self):
        super().__init__("Incident not found")