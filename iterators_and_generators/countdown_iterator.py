class countdown_iterator:

    def __init__(self, count: int):
        self.count = count + 1
        self.stop = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.stop:
            raise StopIteration

        self.count -= 1

        return self.count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")