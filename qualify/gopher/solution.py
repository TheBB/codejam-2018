def optimal_cell(matrix, M, N):
    value = 0
    for m in range(M):
        for n in range(N):
            if matrix[m][n] > value:
                value = matrix[m][n]
                index = (m, n)
            if value == 9:
                return index
    if value == 0:
        return None, None
    return index


def prepare(size):
    if size == 20:
        M, N = 3, 2             # Interior of 5x4
    elif size == 200:
        M, N = 18, 8            # Interior of 20x10

    # Matrix of plots, each cell is the number of unprepared neighbours
    matrix = [[9] * N for _ in range(M)]

    # Indices of prepared cells
    prepared = set()

    while True:
        I, J = optimal_cell(matrix, M, N)
        print(I+2, J+2)
        Ip, Jp = map(int, input().split())
        if Ip == -1 and Jp == -1:
            return False
        if Ip == 0 and Jp == 0:
            return True
        Ip -= 2
        Jp -= 2
        if (Ip, Jp) in prepared:
            continue
        prepared.add((Ip, Jp))
        for ii in (Ip-1, Ip, Ip+1):
            for jj in (Jp-1, Jp, Jp+1):
                if 0 <= ii < M and 0 <= jj < N:
                    matrix[ii][jj] = max(matrix[ii][jj] - 1, 0)


if __name__ == '__main__':
    ncases = int(input())
    for _ in range(ncases):
        size = int(input())
        if not prepare(size):
            break
