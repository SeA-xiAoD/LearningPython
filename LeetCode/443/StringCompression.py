class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if chars == []:
            []
        count = 1
        pos = 0
        while pos < len(chars) - 1:
            if chars[pos] == chars[pos + 1]:
                count += 1
                chars.pop(pos)
            else:
                if count != 1:
                    temp = 1
                    while count > 0:
                        chars.insert(pos + 1, str(count % 10))
                        temp += 1
                        count //= 10
                    count = 1
                    pos += temp
                elif count == 1:
                    pos += 1
        if count != 1:
            while count > 0:
                chars.insert(pos + 1, str(count % 10))
                count //= 10
        return len(chars)
