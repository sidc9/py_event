from event import event
from event import subscriber
from event import publisher

class Ev(event.Event):
    def __init__(self):
        super(Ev, self).__init__("event1111")
    def serialize_payload(self):
        return self.payload
    def deserialize_payload(self, payload):
        return payload

class Disp(subscriber.Subscriber):
    def __init__(self):
        super(Disp, self).__init__("disp")

    def receive_event(self, event_serialized):
        print  "event occured", event_serialized

if __name__ == '__main__':
    ev = Ev()
    p = publisher.Publisher([ev])
    s = Disp()

    p.register(ev, s)
    ev.payload = "hello"
    p.publish(ev)
