class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.items) - 1 <= self.index:
            raise StopIteration

        self.index += 1

        return self.items[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)