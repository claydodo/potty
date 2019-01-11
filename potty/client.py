from krux.random import *

from .profile import *
from .session_pool import *
from .session import *
from .nodes.root_node import RootNode


__all__ = ['PotClient']


class PotClient(object):
    def __init__(self, profile='default'):
        if isinstance(profile, str):
            self.profile = Profile.load(profile)
        elif isinstance(profile, Profile):
            self.profile = profile
        elif isinstance(profile, dict):
            self.profile = Profile(**profile)

        self.sessions = SessionPool()

    @property
    def id(self):
        return self.profile.id

    def __repr__(self):
        return "<{} {}>".format(self.profile.id, self.profile.name)

    def new_session(self):
        # TODO: post create session to server, use the returning info as init parameter
        s = Session(client=self, id=gen_uuid32())
        self.sessions.append(s)
        return s

    def get_session(self, id_or_index):
        pass

    def get_root_node(self):
        return RootNode(self)



