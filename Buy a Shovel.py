def min_shovels(k, r):
    for n in range(1, 11): 
        total_cost = n * k
        if total_cost % 10 == 0 or total_cost % 10 == r:
            print(n)
            return
k, r = map(int, input().split())
min_shovels(k, r)
