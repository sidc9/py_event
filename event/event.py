#!/usr/bin/python

"""
event.py

Classes:
    Event
    Subscriber
    Publisher

"""

import time
import json

class Event(object):
    def __init__(self, name):
        self._payload = {}
        self.name = name
        self.timestamp = None

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, payload_):
        self.timestamp = str(time.time() * 1000)
        self._payload = payload_

    def serialize_payload(self):
        raise NotImplementedError()

    def deserialize_payload(self, payload):
        raise NotImplementedError()

    def serialize(self):
        info = {}
        info["timestamp"] = self.timestamp
        info["name"] = self.name
        info["payload"] = self.serialize_payload()
        return json.dumps(info)

    def deserialize(self, event_serialized):
        info = json.loads(event_serialized)
        self.timestamp = info["timestamp"]
        self.name = info["name"]
        self.payload = self.deserialize_payload(info["payload"])
