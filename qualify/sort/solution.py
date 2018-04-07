if __name__ == '__main__':
    ncases = int(input())
    for c in range(1, ncases + 1):
        _ = input()
        data = list(map(int, input().split()))
        data[::2] = sorted(data[::2])
        data[1::2] = sorted(data[1::2])

        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                print('Case #{}: {}'.format(c, i))
                break
        else:
            print('Case #{}: OK'.format(c))
