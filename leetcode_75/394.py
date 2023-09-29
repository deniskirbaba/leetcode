# class Solution:
#     def decodeString(self, s: str) -> str:
#         res = ""
#         in_br = False
#         k = ""
#         br_str = ""
#         for ch in s:
#             if not in_br:
#                 if ch.isalpha():
#                     res += ch
#                 elif ch.isdigit():
#                     k += ch
#                 elif ch == '[':
#                     in_br = True
#             else:
#                 if ch.isalpha():
#                     br_str += ch
#                 elif ch == ']':
#                     res += br_str * int(k)
#                     in_br = False
#                     k = ""
#                     br_str = ""
#         return res



class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        cur_str, cur_k = "", ""
        for ch in s:
            if ch.isalpha():
                cur_str += ch
            elif ch.isdigit():
                cur_k += ch
            elif ch == '[':
                stack.append((cur_str, int(cur_k)))
                cur_str, cur_k = "", ""
            else:
                last_str, last_k = stack.pop()
                cur_str = last_str + cur_str * last_k
        return cur_str