def solve():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    magnets = input_data[1:]
    groups = 1
    for i in range(1, n):
        if magnets[i] != magnets[i - 1]:
            groups += 1
            
    sys.stdout.write(str(groups))

if __name__ == "__main__":
    solve()
