class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """



        # Step 1: Frequency Map
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Create Buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into their frequency bucket
        for num, count in freq.items():
            bucket[count].append(num)

        # Step 4: Traverse buckets from highest frequency
        result = []

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
        