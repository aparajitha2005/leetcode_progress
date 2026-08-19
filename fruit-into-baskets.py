class Solution(object):
    def totalFruit(self, fruits):
        count = {}
        left = 0
        maximum = 0
        for right in range (len(fruits)):
            if fruits[right] in count:
                count[fruits[right]] += 1
            else:
                count[fruits[right]] = 1

            while len(count) > 2:
                if fruits[left] in count:
                    count[fruits[left]] -= 1
                    if count[fruits[left]] == 0:
                        del count[fruits[left]]
                left += 1
            
            maximum = max(right - left +1, maximum)
        return maximum
        



        """
        :type fruits: List[int]
        :rtype: int
        """
        