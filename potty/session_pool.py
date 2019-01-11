class SessionPool(list):
    def __repr__(self):
        return "\n".join(["{:>6}\t{}".format(i, session) for (i, session) in enumerate(self)])

