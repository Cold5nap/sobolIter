class Iteration:
    def __iter__(self):
        return self

    def __init__(self, data):
        self.data = data
        self.counter = 0

    def __next__(self):
        if self.counter < self.data:
            ret = self.counter
            self.counter += 1
            return ret
        else:
            raise StopIteration
