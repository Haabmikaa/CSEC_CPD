def minimum_road_width():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))
    
    total_width = 0
    for ai in heights:
        if ai > h:
            total_width += 2
        else:
            total_width += 1
            
    print(total_width)

if __name__ == '__main__':
    minimum_road_width()
