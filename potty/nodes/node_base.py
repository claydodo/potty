class PotNodeBase(object):
    def __init__(self, *args, **kwargs):
        pass

    def ls(self):
        raise NotImplementedError()

    def cd(self, path):
        raise NotImplementedError()

    def select(self):
        raise NotImplementedError()

    def fetch(self):
        raise NotImplementedError()
