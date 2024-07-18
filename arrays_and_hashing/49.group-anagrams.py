class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key: sorted word, value: actual word
        groups = {}

        for word in strs:
            sorted_str = str(sorted(word))
            if sorted_str in groups:
                groups[sorted_str].append(word)
            else:
                groups[sorted_str] = [word]

        return groups.values()

