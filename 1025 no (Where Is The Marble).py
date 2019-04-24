


bin_search(L, e):


counter = 0


while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    else:
        marbles = []
        for i in range(x):
            marble = int(input())
            marbles.append(marble)

        counter += 1

        for j in range(y):
            query = int(input())
            print('CASE# {}'.format(counter))
            if query in marbles:
                print('{} found at {}'.format(query, sorted(marbles).index(query) + 1))
            else:
                print('{} not found'.format(query))
