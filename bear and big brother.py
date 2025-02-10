def bear_and_big_brother():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    print(years)

if __name__ == '__main__':
    bear_and_big_brother()
