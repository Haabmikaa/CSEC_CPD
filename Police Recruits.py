def solve():
    import sys
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    events = list(map(int, input_data[1:]))
    
    officers = 0
    untreated = 0
    
    for event in events:
        if event == -1:
            if officers > 0:
                officers -= 1
            else:
                untreated += 1
        else:
            officers += event
    
    sys.stdout.write(str(untreated))

if __name__ == "__main__":
    solve()
