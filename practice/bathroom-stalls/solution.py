from itertools import count


def power(n):
    for i in count():
        if 2**i > n:
            return 2**(i-1)


if __name__ == '__main__':
    ncases = int(input())
    for i in range(1, ncases+1):
        nstalls, nguests = map(int, input().split())
        nblocks = power(nguests)
        total = nstalls - nblocks + 1
        baseline = total // nblocks
        rest = total - baseline * nblocks
        index = nguests - nblocks
        gap = baseline + 1 if index < rest else baseline
        if gap % 2 == 1:
            print('Case #{}: {} {}'.format(i, gap//2, gap//2))
        else:
            print('Case #{}: {} {}'.format(i, gap//2, gap//2-1))
