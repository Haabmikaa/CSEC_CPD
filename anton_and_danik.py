def anton_and_danik():
    n = int(input().strip())
    s = input().strip()
    
    # Count the wins for Anton and Danik
    anton_wins = s.count('A')
    danik_wins = s.count('D')
    
    # Determine and print the result based on the counts
    if anton_wins > danik_wins:
        print("Anton")
    elif danik_wins > anton_wins:
        print("Danik")
    else:
        print("Friendship")

if __name__ == '__main__':
    anton_and_danik()
