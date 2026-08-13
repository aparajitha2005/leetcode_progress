class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        satisfied = 0
        left = 0
        right = minutes - 1
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        save = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                save += customers[i]
        maxsave = save
        while right < len(customers) - 1 and left <= right:
            if grumpy[left] == 1:
                save -= customers[left]
            left += 1
            right += 1
            if grumpy[right] == 1:
                save += customers[right]
            if save > maxsave:
                maxsave = save
        score = satisfied + maxsave
        return score
        

            


                

        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        