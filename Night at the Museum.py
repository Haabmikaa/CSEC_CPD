def solve():
    import sys
    input_data = sys.stdin.read().strip()
    
    current_position = 'a' 
    total_rotations = 0
    
    for char in input_data:
        distance = abs(ord(char) - ord(current_position))
        total_rotations += min(distance, 26 - distance)
     
        current_position = char
    
    sys.stdout.write(str(total_rotations) + "\n")

if __name__ == "__main__":
    solve()
