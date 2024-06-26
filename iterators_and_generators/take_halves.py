def solution():

    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        for number in integers():
            yield number / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

