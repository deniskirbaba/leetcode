class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) - len(word2):
            return False
        
        char_freq_1 = dict()
        char_freq_2 = dict()
        for ch1, ch2 in zip(word1, word2):
            char_freq_1[ch1] = char_freq_1.get(ch1, 0) + 1
            char_freq_2[ch2] = char_freq_2.get(ch2, 0) + 1

        if set(char_freq_1.keys()) - set(char_freq_2.keys()):
            return False
        
        freq_freq_1 = dict()
        freq_freq_2 = dict()
        for ch in set(word1):
            freq_freq_1[char_freq_1[ch]] = freq_freq_1.get(char_freq_1[ch], 0) + 1
            freq_freq_2[char_freq_2[ch]] = freq_freq_2.get(char_freq_2[ch], 0) + 1
        for freq_1 in freq_freq_1:
            if freq_freq_1[freq_1] != freq_freq_2.get(freq_1, None):
                return False
            
        return True