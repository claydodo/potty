from krux.types import Singleton
from .client import PotClient
from .session_pool import SessionPool


class ClientPool(Singleton):
    clients = {}

    def get(self, profile_id):
        if profile_id not in self.clients:
            self.clients[profile_id] = PotClient(profile=profile_id)
        return self.clients[profile_id]

    @property
    def sessions(self):
        pool = SessionPool()
        for client in self.clients.values():
            pool.extend(client.sessions)
        return pool

