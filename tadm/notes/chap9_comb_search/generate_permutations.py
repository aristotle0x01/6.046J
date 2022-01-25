# the algorithm design manual backtrack permutations
class GenPermutations:
    # Constructor
    def __init__(self):
        self.finished = False

    def is_a_solution(self, a: [], k: int, n: int):
        return k == n

    def process_solution(self, a: [], k: int, n: int):
        print('{', end='')
        for i in range(k):
            print('{0}'.format(a[i]), end='')
        print('}\n', end='')

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        for i in range(1, n+1):
            if i not in a:
                c.append(i)

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


b = GenPermutations()
b.backtrack([], 0, 4)
