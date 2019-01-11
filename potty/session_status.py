class SessionStatus(object):
    def __init__(self, session_id, is_alive=None, expire_dt=None, **kwargs):
        self.session_id = session_id
        self.is_alive = is_alive
        self.expire_dt = expire_dt

