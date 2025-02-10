def solve():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    cards = list(map(int, input_data[1:]))
  
    sereja_score = 0
    dima_score = 0
    left, right = 0, n - 1
    turn = 0
  
    while left <= right:
        if cards[left] >= cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1

        if turn == 0:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card

        turn = 1 - turn

    sys.stdout.write(f"{sereja_score} {dima_score}")

if __name__ == "__main__":
    solve()
