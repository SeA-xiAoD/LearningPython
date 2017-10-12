class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        length_ransom = len(ransomNote)
        length_magzione = len(magazine)
        ransom_dir = {}
        magazine_dir = {}
        for i in range(0, length_ransom):
            try:
                ransom_dir[ransomNote[i]] += 1
            except:
                ransom_dir[ransomNote[i]] = 1
        for i in range(0, length_magzione):
            try:
                magazine_dir[magazine[i]] += 1
            except:
                magazine_dir[magazine[i]] = 1
        for key in ransom_dir.keys():
            try:
                if ransom_dir[key] - magazine_dir[key] > 0:
                    return False
            except:
                return False
        return True
