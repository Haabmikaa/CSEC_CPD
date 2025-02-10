for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            # Calculate the Manhattan distance to the center (2,2)
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            break
