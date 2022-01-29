from collections import deque


# https://leetcode.com/problems/brace-expansion-ii/
class Solution:
    # Constructor
    def __init__(self):
        self.finished = False
        self.expansions = []
        self.expression = ''
        self.current_index = 0
        self.n = 0

    def initialize(self, expression: str):
        self.finished = False
        self.expansions = []
        self.expression = expression
        self.current_index = 0
        self.n = len(expression)

    def is_a_solution(self, a: [], k: int, n: int):
        if self.current_index == n:
            return True

        return False

    def process_solution(self, a: [], k: int, n: int):
        s = ''.join(a)
        if s not in self.expansions:
            self.expansions.append(s)
        # print('{', end='')
        # for i in a:
        #     print(i, end='')
        # print('}\n', end='')

    def make_move(self, a: [], k: int, n: int):
        return

    def unmake_move(self, a: [], k: int, n: int):
        return

    # type = 1 for a prefix '{'
    # type = 2 for a prefix ','
    # a flatmap is needed in case of '{' or ',*'
    def flatmap(self, start: int):
        if start >= self.n:
            return [], start

        # Input: expression = "{a,b}{c,{d,e}}"
        # Output: ["ac", "ad", "ae", "bc", "bd", "be"]
        # Input: expression = "{{a,z},a{b,c},{ab,z}}"
        # Output: ["a","ab","ac","z"]

        result = []
        stack = deque()
        stack.append(self.expression[start])
        start += 1
        while start < self.n and len(stack) > 0:
            i = start

            if self.expression[i] == '{':
                tmp = ""
                while len(stack) > 0 and stack[-1].isalpha():
                    tmp = stack.pop() + tmp
                array, inner_start = self.flatmap(start)
                for i in range(len(array)):
                    array[i] = tmp + array[i]

                if (i - 1) >= 0 and self.expression[i - 1] == ',':
                    result.extend(array)
                if (i - 1) >= 0 and self.expression[i - 1] != ',':
                    if len(result) == 0:
                        result = array
                    else:
                        tmp = []
                        for r in result:
                            for t in array:
                                tmp.append(r + t)
                        result = tmp
                start = inner_start
            elif self.expression[i] == ',':
                if (i - 1) >= 0 and self.expression[i - 1].isalpha():
                    tmp = ""
                    while len(stack) > 0 and stack[-1].isalpha():
                        tmp = stack.pop() + tmp
                    if len(tmp) > 0:
                        if len(result) == 0:
                            result.append(tmp)
                        else:
                            for i in range(len(result)):
                                result[i] = result[i] + tmp

                array, inner_start = self.flatmap(start)
                result.extend(array)
                start = inner_start
            elif self.expression[i] == '}':
                tmp = ""
                while stack[-1].isalpha():
                    tmp = stack.pop() + tmp
                if len(stack) > 0 and stack[-1] == '{':
                    start += 1
                    stack.pop()
                if len(stack) > 0 and stack[-1] == ',':
                    stack.pop()
                if len(tmp) > 0:
                    if (i-len(tmp)-1) >= 0 and self.expression[i-len(tmp)-1] == ',':
                        result.extend([tmp])
                    else:
                        for j in range(len(result)):
                            result[j] = result[j] + tmp
                break
            else:
                stack.append(self.expression[i])
                start += 1

        return result, start

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        if self.current_index >= n:
            return

        if self.expression[self.current_index] == '{':
            candidates, count = self.flatmap(self.current_index)
            self.current_index = count
            c.extend(candidates)
        else:
            tmp = ""
            i = self.current_index
            while i < self.n and self.expression[i].isalpha():
                tmp += self.expression[i]
                i += 1
            c.append(tmp)
            self.current_index = i

    def backtrack(self, a: [], k: int, n: int):
        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            candidates = []
            old = self.current_index
            self.construct_candidates(a, k, n, candidates)
            a.append('')
            for s in candidates:
                a[k - 1] = s

                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)

                if self.finished:
                    return
            self.current_index = old
            del a[-1]

    def braceExpansionII(self, expression: str) -> list[str]:
        if len(expression) == 0:
            return []

        a = []
        self.initialize(expression)
        self.backtrack(a, 0, len(expression))
        return sorted(self.expansions)


g = Solution()
# Input: expression = "{a,b}{c,{d,e}}"
# Output: ["ac","ad","ae","bc","bd","be"]

# Input: expression = "{{a,z},a{b,c},{ab,z}}"
# Output: ["a","ab","ac","z"]

# ["a","aera","aerg","aeria","aern","aero","aeru","aerw","aerx","er","iaera","iaerg","iaeria","iaern","iaero","iaeru","iaerw","iaerx","oera","oerg","oeria","oern","oero","oeru","oerw","oerx","wera","werg","weria","wern","wero","weru","werw","werx","xera","xerg","xeria","xern","xero","xeru","xerw","xerx"]
# ['a', 'area', 'areg', 'areia', 'aren', 'areo', 'areu', 'arew', 'arex', 'iarea', 'iareg', 'iareia', 'iaren', 'iareo', 'iareu', 'iarew', 'iarex', 'orea', 'oreg', 'oreia', 'oren', 'oreo', 'oreu', 'orew', 'orex', 're', 'wrea', 'wreg', 'wreia', 'wren', 'wreo', 'wreu', 'wrew', 'wrex', 'xrea', 'xreg', 'xreia', 'xren', 'xreo', 'xreu', 'xrew', 'xrex']
# print(g.braceExpansionII("{a,{a,{x,ia,o},w}er{n,{g,{u,o}},{a,{x,ia,o},w}},er}"))
print(g.braceExpansionII("{{a,{x,ia,o},w},er,a{x,ia,o}w}"))