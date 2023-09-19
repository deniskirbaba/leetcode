class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowels = len([ch for ch in s[:k] if ch in vowels])
        cur_vowels = max_vowels
        for i in range(k, length):
            if s[i - k] in vowels:
                cur_vowels -= 1
            if s[i] in vowels:
                cur_vowels += 1
            max_vowels = max(max_vowels, cur_vowels)
        return max_vowels