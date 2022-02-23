# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s) -> int:
        if len(s) == 0:
            return 0

        tmp = ''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            # (-1+2...
            if s[i] == '-' and len(tmp) > 0 and tmp[-1] == '(':
                tmp = tmp + '0'
            tmp = tmp + s[i]
        # -*...
        if len(tmp) > 0 and tmp[0] == '-':
            tmp = '0' + tmp

        return self.calculate_rec(tmp, 0, len(tmp)-1)

    def calculate_rec(self, s, start: int, end: int) -> int:
        if start > end:
            return 0

        # accumulative value
        acc = 0
        operator = '+'

        j = start
        while j <= end:
            if s[j] == '(':
                stack = [j]
                for i in range(j+1, end+1):
                    if s[i] == '(':
                        stack.append(i)
                        continue
                    if s[i] == ')':
                        left_parentheses_index = stack.pop()
                        if len(stack) == 0:
                            tv = self.calculate1(s, left_parentheses_index+1, i-1)
                            tj = i+1
                            break
                if operator == '+':
                    acc = acc + tv
                if operator == '-':
                    acc = acc - tv
                j = tj
            else:
                t_value = 0
                while j <= end and s[j].isdigit():
                    t_value = 10 * t_value + int(s[j])
                    j = j + 1
                if operator == '+':
                    acc = acc + t_value
                if operator == '-':
                    acc = acc - t_value

            if j > end:
                break

            operator = s[j]
            j = j + 1

        return acc

    def calculate_mine(self, s) -> int:
        if len(s) == 0:
            return 0

        tmp = ''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            # (-1+2...
            if s[i] == '-' and len(tmp) > 0 and tmp[-1] == '(':
                tmp = tmp + '0'
            tmp = tmp + s[i]
        # -*...
        if len(tmp) > 0 and tmp[0] == '-':
            tmp = '0' + tmp

        return self.calculate_inner(tmp)

    # "1+(1+(4+2))-3"
    # 类似函数调用栈，每当遇到'('，则保留之前的结果和操作符
    # 当遇到')'则为一次调用结束，pop之前保留结果与操作符，与本次结果进行计算
    # (1, '+')    -> 1+7 = 8
    #   (1, '+') -> 1+6=7
    #     4+2 -> 6
    def calculate_inner(self, s) -> int:
        operator = '+'
        stack = []
        acc = 0

        end = len(s)
        i = 0
        while i < end:
            if s[i].isdigit():
                t_v = 0
                while i < end and s[i].isdigit():
                    t_v = 10*t_v + int(s[i])
                    i = i + 1

                if operator == '+':
                    acc = acc + t_v
                else:
                    acc = acc - t_v
            elif s[i] in ['+', '-']:
                operator = s[i]
                i = i + 1
            elif s[i] == '(':
                stack.append((acc, operator))
                acc, operator = 0, '+'
                i = i + 1
            elif s[i] == ')':
                (pre_acc, pre_operator) = stack.pop()
                if pre_operator == '+':
                    acc = pre_acc + acc
                else:
                    acc = pre_acc - acc

                operator = '+'
                i = i + 1

        return acc

    # reference implementation
    def calculate_ref(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10 * num + int(ss)
            elif ss in ["-", "+"]:
                res += sign * num
                num = 0
                sign = [-1, 1][ss == "+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign


g = Solution()
s1 = "(1+(4+5+2)-3)-(-(6-8)+1)"
s2 = "1-2-3"
print(g.calculate_mine(s1))
print(g.calculate_mine(s2))
print(g.calculate_ref(s1))