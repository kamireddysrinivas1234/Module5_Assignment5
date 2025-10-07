from app.history import History

class DummyObs:
    def __init__(self):
        self.count = 0
    def notify(self, df):
        self.count += 1

def test_attach_detach_observer():
    h = History()
    d = DummyObs()
    h.attach(d)
    h.add("add", 1, 2, 3)
    assert d.count == 1
    h.detach(d)
    h.add("add", 2, 3, 5)
    assert d.count == 1
