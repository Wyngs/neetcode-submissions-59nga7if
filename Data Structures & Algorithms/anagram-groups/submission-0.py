class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def make_tuple(word):
            freq=[0]*26
            for i in word:
                if freq[ord(i)-ord('a')]==0:
                    freq[ord(i)-ord('a')] = word.count(i)
            return tuple(freq)
        
        wordmap ={}

        for i in strs:
            wordfreq = make_tuple(i)
            if wordfreq not in wordmap:
                wordmap[wordfreq] = []
            wordmap[wordfreq].append(i)
        
        return list(wordmap.values())

            
        