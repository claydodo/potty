from krust.pather import Pather

__all__ = ['Profile']

POTTY_PATHER = Pather(env_var='POTTY_PATH', paths=['/etc/potty/profiles', '~/.potty/profiles', './potty/profiles'])
PROFILE_ATTRS = ('id', 'name', 'url', 'apikey')


class Profile(object):
    @classmethod
    def load(cls, profile_name):
        fname = POTTY_PATHER.get(profile_name)
        if fname is None:
            raise RuntimeError("Cannot find potty profile {}".format(profile_name))

        para = {"id": profile_name, "name": "", "url": "", "apikey": "", "desc": ""}

        with open(fname) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or '=' not in line:
                    continue
                attr, val = [tk.strip() for tk in line.split("=", 1)]
                if attr in PROFILE_ATTRS:
                    para[attr] = val

        return cls(**para)

    def __init__(self, id, name, url, apikey, desc=""):
        self.id = id
        self.name = name
        self.url = url
        self.apikey = apikey
        self.desc = desc

