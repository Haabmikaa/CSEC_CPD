def solve():
    import sys
    input_data = sys.stdin.read().splitlines()
    
    n = int(input_data[0])  
    teams = [tuple(map(int, line.split())) for line in input_data[1:]] 
    
    count = 0  

    for i in range(n): 
        for j in range(n): 
            if i != j and teams[i][0] == teams[j][1]: 
                count += 1

    print(count) 

if __name__ == "__main__":
    solve()
