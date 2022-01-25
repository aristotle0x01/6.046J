# the algorithm design manual backtrack subsets
class GenSubsets:
    # Constructor
    def __init__(self):
        self.finished = False

    def is_a_solution(self, a: [], k: int, n: int):
        return k == n

    def process_solution(self, a: [], k: int, n: int):
        print('{', end='')
        for i in range(k):
            if a[i] == 1:
                print('{0}'.format(i+1), end='')
        print('}\n', end='')
        return

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        c.append(1)
        c.append(0)
        return

    def make_move(self, a: [], k: int, n: int):
        return

    def unmake_move(self, a: [], k: int, n: int):
        return

    def backtrack(self, a: [], k: int, n: int):
        candidates = []

        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            a.append(0)
            self.construct_candidates(a, k, n, candidates)
            for i in range(len(candidates)):
                a[k-1] = candidates[i]
                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)

                if self.finished:
                    return

            del a[-1]


b = GenSubsets()
b.backtrack([], 0, 3)
