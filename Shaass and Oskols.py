def shaass_and_oskols():
    n = int(input().strip())
    wires = list(map(int, input().split()))
    m = int(input().strip())
    
    for _ in range(m):
        x, y = map(int, input().split())
        index = x - 1 
        left = y - 1
        right = wires[index] - y

        if index - 1 >= 0:
            wires[index - 1] += left
        if index + 1 < n:
            wires[index + 1] += right
        
        wires[index] = 0
    for count in wires:
        print(count)

if __name__ == '__main__':
    shaass_and_oskols()
