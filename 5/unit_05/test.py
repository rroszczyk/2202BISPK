from unittest.mock import patch

class ControllerInterface(object):
    def __init__(self):
        raise NotImplementedError

    def callMailer(self, data):
        raise NotImplementedError

class DummyController(ControllerInterface):
    def __init__(self, mailer):
        self.mailer = mailer

    def callMailer(self, data):
        self.mailer.send(data)

class Mailer():
    def send(self, data):
        pass


@patch.object(Mailer, "send")
def test_controller(mock_send):
    conroller = DummyController(Mailer())
    data = {}
    conroller.callMailer(data)
    mock_send.assert_called_with(data)

test_controller()