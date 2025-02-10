def final_position(s, t):
    index = 0  

    for move in t:
        if index < len(s) and s[index] == move:
            index += 1 

    print(index + 1)  

s = input().strip()
t = input().strip()

final_position(s, t)
