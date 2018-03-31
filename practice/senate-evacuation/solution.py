def majority_exists(members):
    threshold = sum(members) // 2
    return any(m > threshold for m in members)


def empty(members):
    return all(m == 0 for m in members)


def largest(members):
    i, n = -1, 0
    for ii, nn in enumerate(members):
        if nn > n:
            n = nn
            i = ii
    assert i >= 0
    return i


def evacuate(members):
    while not empty(members):
        # Pick a senator from the largest party
        i1 = largest(members)
        members[i1] -= 1

        # If empty, finish
        if empty(members):
            yield (i1,)
            return

        # Pick another senator from the largest party
        i2 = largest(members)
        members[i2] -= 1

        # If empty, finish
        if empty(members):
            yield (i1,i2)
            return

        # Ensure that there isn't a majority
        if majority_exists(members):
            members[i2] += 1
            yield (i1,)
            continue

        yield (i1,i2)


if __name__ == '__main__':
    ncases = int(input())
    names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, ncases + 1):
        input()                 # Number of parties
        members = list(map(int, input().split()))
        plan = ' '.join(''.join(names[i] for i in step) for step in evacuate(members))
        print('Case #{}: {}'.format(i, plan))
