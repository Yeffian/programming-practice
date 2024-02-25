import math

# Will Ness's algorithim
class Primes:
    @staticmethod
    def stream():
            import itertools
            yield from (2, 3, 5, 7)
            D = {}
            ps = Primes.stream()
            next(ps)
            p = next(ps)
            assert p == 3
            psq = p*p
            for i in itertools.count(9, 2):
                # composite number
                if i in D:
                    step = D.pop(i)
                # prime number
                elif i < psq:
                    yield i
                    continue
                # composite again
                else:
                    assert i == psq
                    step = 2*p
                    p = next(ps)
                    psq = p*p
                i += step
                while i in D:
                    i += step
                D[i] = step
