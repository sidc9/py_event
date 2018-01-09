"""
subscriber.py
"""
class Subscriber(object):
    def __init__(self, name):
        self.name = name
    def receive_event(self, event_serialized):
        raise NotImplementedError()
