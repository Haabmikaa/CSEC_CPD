def min_horseshoes_needed(s1, s2, s3, s4):
    unique_colors = len(set([s1, s2, s3, s4]))
    print(4 - unique_colors)

s1, s2, s3, s4 = map(int, input().split())
min_horseshoes_needed(s1, s2, s3, s4)
