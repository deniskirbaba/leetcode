class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_char = chars[0]
        cur_char_st_idx = 0
        cur_n = 1
        cur_idx = 1
        flag = True
        while flag:
            try:
                new_char = chars[cur_idx]
            except IndexError:
                new_char = None
                flag = False
            if new_char == cur_char:
                cur_n += 1
            else:
                if cur_n == 2:
                    chars[cur_idx - 1] = "2"
                elif cur_n != 1:
                    n_n = len(str(cur_n))
                    del chars[cur_char_st_idx + 1 + n_n:cur_char_st_idx + cur_n]
                    for idx, ccc in enumerate(str(cur_n)):
                        chars[cur_char_st_idx + 1 + idx] = ccc
                    cur_idx -= (cur_n - 1 - n_n)
                cur_char = new_char
                cur_char_st_idx = cur_idx
                cur_n = 1
            cur_idx += 1
        return len(chars)