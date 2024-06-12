def fibonacci():
    n = 0
    m = 1

    while True:
        yield n
        n, m = m, m + n


generator = fibonacci()
for i in range(5):
    print(next(generator))
