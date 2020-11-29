class Buffer(object):
    def __init__(self, buf):
        self.buf = buf

    def write(self, s):
        ll = s.split('\n')
        self.buf[-1] += ll[0]
        for l in ll[1:]:
            self.buf.append(l)

    def clear(self):
        del self.buf[:]
