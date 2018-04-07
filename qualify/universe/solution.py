def candidate(damage):
    for i in range(len(damage) - 1):
        if damage[i] > damage[i+1]:
            return i
    if damage[-1] > 1:
        return len(damage) - 1
    return None


if __name__ == '__main__':
    ncases = int(input())
    for i in range(1, ncases + 1):
        threshold, program = input().split()
        threshold = int(threshold)

        damage = []
        power = 1
        for c in program:
            if c == 'S':
                damage.append(power)
            else:
                power *= 2

        nhacks = 0
        total = sum(damage)
        damage = damage[::-1]
        while total > threshold:
            c = candidate(damage)
            if c is None:
                break
            damage[c] //= 2
            total -= damage[c]
            nhacks += 1

        if total > threshold:
            print('Case #{}: IMPOSSIBLE'.format(i))
        else:
            print('Case #{}: {}'.format(i, nhacks))
