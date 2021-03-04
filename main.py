EPSILON = 0.00001
p0 = 0.5073
n0 = 23
d0 = 365


def p(n, d):
    pc = p0
    nc = n0
    dc = d0

    if n-n0 and d-d0:
        DELTA = abs((d - d0) / (n - n0)) * EPSILON

        nstep = round((n - n0) / EPSILON)
        nsign = round(abs(nstep) / nstep)
        dstep = round((d - d0) / DELTA)
        dsign = round(abs(dstep) / dstep)
        assert abs(nstep) == abs(dstep)
        print(f'steps: {nstep}')

        while nstep or dstep:
            pc += nsign * EPSILON * p_n(nc, dc, pc) + dsign * DELTA * p_d(nc, dc, pc)
            nc += EPSILON
            nstep -= nsign
            dc += DELTA
            dstep -= dsign
    elif n-n0:
        nstep = round((n - n0) / EPSILON)
        nsign = round(abs(nstep) / nstep)
        print(f'steps: {nstep}')

        while nstep:
            pc += nsign * EPSILON * p_n(nc, dc, pc)
            nc += EPSILON
            nstep -= nsign
    elif d-d0:
        dstep = round((d - d0) / EPSILON)
        dsign = round(abs(dstep) / dstep)
        assert abs(dstep) == abs(dstep)
        print(f'steps: {dstep}')

        while dstep:
            pc += dsign * EPSILON * p_d(nc, dc, pc)
            dc += EPSILON
            dstep -= dsign

    return pc


def p_n(n, d, p):
    return n * (1 - p) / d


def p_d(n, d, p):
    return -n * n * (1 - p) / (2 * d * d)


if __name__ == '__main__':
    print(f'p(24, 358) = {p(24, 358)}')
    print(f'p(25, 365) = {p(25, 365)}')
    print(f'p(23, 344) = {p(23, 344)}')
    print(f'grad_p(23, 365) = ({p_n(n0, d0, p0)}, {p_d(n0, d0, p0)})')

