name = "potty"

from krux.types.check import is_integer
from .client_pool import ClientPool

__all__ = [
    'connect',
    'new_session', 'ls_sessions', 'gcs', 'scs',
    'ns', 'lss', 'gcs', 'scs',
    'ls', 'cd', 'select',
    'fetch',
]

_pot_client_pool = ClientPool()
_pot_session_pool = None
_pot_current_session = None


def connect(profile='default'):
    client = _pot_client_pool.get(profile)
    ls_sessions()
    return client


def ls_sessions():
    global _pot_session_pool
    _pot_session_pool = _pot_client_pool.sessions
    return _pot_session_pool


def new_session(profile='default'):
    global _pot_current_session
    client = _pot_client_pool.get(profile)
    _pot_current_session = client.new_session()
    ls_sessions()
    return _pot_current_session


def get_current_session():
    return _pot_current_session


def set_current_session(session):
    global _pot_session_pool
    global _pot_current_session

    if _pot_session_pool is None:
        ls_sessions()

    if isinstance(session, str):
        candidates = []
        for s in _pot_session_pool:
            if s.id.startswith(session):
                candidates.append(s)
        if len(candidates) == 0:
            print("No matching session!")
        elif len(candidates) == 1:
            _pot_current_session = candidates[0]
        else:
            print("More than one matching sessions!")
    elif is_integer(session):
        if 0 <= session < len(_pot_session_pool):
            _pot_current_session = _pot_session_pool[session]
        else:
            print("Invalid index!")
    else:
        print("Parameter should be integer or string!")

    return _pot_current_session


def ls():
    get_current_session().ls()


def cd(path):
    get_current_session().cd(path)


def select():
    return get_current_session().select()


def undo():
    return get_current_session().undo()


def redo():
    return get_current_session().redo()


def fetch():
    return get_current_session().fetch()


# Alias
ns = new_session
lss = ls_sessions
gcs = get_current_session
scs = set_current_session
