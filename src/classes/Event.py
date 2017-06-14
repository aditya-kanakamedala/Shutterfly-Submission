'''
    Generic event object containing event attributes event_type, event_verb and additional_data
'''


class Event:
    event_type = ""
    event_verb = ""
    additional_data = {}

    def __init__(self, event_type, event_verb, additional_data):
        self.event_type = event_type
        self.event_verb = event_verb
        self.additional_data = additional_data
