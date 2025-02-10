s = input().strip()

upper_count = sum(1 for char in s if char.isupper())
lower_count = sum(1 for char in s if char.islower())

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
