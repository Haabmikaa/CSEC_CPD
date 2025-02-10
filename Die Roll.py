import math

def die_roll_probability(Y, W):
    max_roll = max(Y, W)
    favorable = 6 - max_roll + 1
    gcd = math.gcd(favorable, 6) 
    print(f"{favorable // gcd}/{6 // gcd}")

Y, W = map(int, input().split())
die_roll_probability(Y, W)
