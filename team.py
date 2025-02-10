def team():
    n = int(input().strip())
    problems_solved = 0
    for _ in range(n):
        # Read the three integers representing whether each friend is sure about the solution
        opinions = list(map(int, input().split()))
        # If at least two friends are sure, count this problem
        if sum(opinions) >= 2:
            problems_solved += 1
    print(problems_solved)

if __name__ == '__main__':
    team()
