
class Session(object):
    def __init__(self, client, id):
        self.client = client
        self.id = id

        self.history = [client.get_root_node()]
        self.pos = 0

    def __repr__(self):
        return '{} @{}'.format(self.id, self.client)

    @property
    def status(self):
        return self.client.get_session_status(id)

    @property
    def current_node(self):
        return self.history[self.pos]

    def is_alive(self):
        self.client.get_session_status(id)

    def ls(self):
        return self.current_node.ls()

    def cd(self, path):
        new_node = self.current_node.cd(path)
        self.history[self.pos+1:] = new_node
        return new_node

    def select(self):
        new_node = self.current_node.select()
        self.history[self.pos+1:] = new_node
        return new_node

    def undo(self):
        if self.pos > 0:
            self.pos -= 1
        else:
            print("Cannot go beyond the first history record!")
        return self.current_node

    def redo(self):
        if self.pos <= len(self.history)-2:
            self.pos += 1
        else:
            print("Cannot go beyond the last history record!")
        return self.current_node

    def fetch(self):
        return self.current_node.fetch()
