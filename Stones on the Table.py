def solve():
    import sys
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    s = input_data[1].strip()
    remove_count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            remove_count += 1
    sys.stdout.write(str(remove_count))

if __name__ == "__main__":
    solve()
