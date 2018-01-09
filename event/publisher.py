"""
publisher.py
"""

class Publisher(object):
    def __init__(self, events):
        self.events = dict()
        for event in events:
            self.events[event] = dict()

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, sub, callback=None):
        if callback is None:
            callback = getattr(sub, 'receive_event')
        subs = self.get_subscribers(event)
        subs[sub] = callback

    def unregister(self, event, sub):
        del self.events[event][sub]

    def publish(self, event):
        for ev in self.events[event]:
            callback = self.events[event][ev]
            event_str = event
            event_str = event.serialize()
            callback(event_str)
