class Solution(object):
    def minimumRecolors(self, blocks, k):
        count = 0
        left = 0
        right = k - 1
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        mincount = count
        while right < len(blocks) - 1 and left <= right:
            if blocks[left] == 'W':
                count -= 1
            left += 1
            right += 1
            if blocks[right] == 'W':
                count += 1
            if count < mincount:
                mincount = count
        return mincount 
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        