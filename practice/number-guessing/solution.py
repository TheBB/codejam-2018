def case():
    lo, hi = map(int, input().split())
    maxguesses = int(input())

    for _ in range(maxguesses):
        if (lo + hi) % 2 == 1:
            guess = (lo + hi + 1) // 2
        else:
            guess = (lo + hi) // 2

        print(guess)
        verdict = input()
        if verdict == 'TOO_SMALL':
            lo = guess
        elif verdict == 'TOO_BIG':
            hi = guess - 1
        else:
            return verdict == 'CORRECT'


if __name__ == '__main__':
    ncases = int(input())
    for _ in range(ncases):
        if not case():
            break
