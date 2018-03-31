if __name__ == '__main__':
    ncases = int(input())
    for i in range(1, ncases + 1):
        destination, nhorses = map(int, input().split())
        max_time = 0.0
        for _ in range(nhorses):
            pos, speed = map(int, input().split())
            time = (destination - pos) / speed
            max_time = max(max_time, time)
        my_speed = destination / max_time
        print('Case #{}: {}'.format(i, my_speed))
