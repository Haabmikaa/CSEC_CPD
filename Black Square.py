def solve():
    import sys
    input_data = sys.stdin.read().split()
    
    a = list(map(int, input_data[:4]))
    
    s = input_data[4].strip()

    total_calories = sum(a[int(ch) - 1] for ch in s)
    
    sys.stdout.write(str(total_calories))

if __name__ == "__main__":
    solve()
