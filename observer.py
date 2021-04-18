from unittest import TestCase


class TestMonitored(TestCase):

    def test_monitored(self):

        p = Monitored()

        m = Monitor(p)

        m.notifiy("Test")

class Monitored():

    def __init__(self):

        self._monitors = []

    def register_monitor(self, monitor):

        self._monitors.append(monitor)

    def notify_event(self, event):

        for m in self._monitors:
            m.notify(self, event)


class Monitor():

    def __init__(self, monitored):

        monitored.register_monitor(self)

    def notifiy(self, event):

        print("Event {}".format(event))
    




