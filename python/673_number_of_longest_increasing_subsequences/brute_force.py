from bisect import bisect_left
from typing import List
"""
This solution first determines the length of longest increasing subsequence by calculating
length using lis_tails which stores for each index, the invariant is 
lis_tails[j] where j<=i stores the smallest value that could be part of some longest 
increasing subsequence 
7 8 2 9 10 lets say is input then
lis_tails for i = 0 to 4 is as follows
i=0 -> [7]
i=1 -> [7,8] observe that 7 and 8 are smallest values of increasing subsequence till index i=1
i=2 -> [2,8] at this point we replace 7 with 2 eventhoug 2 is not part of a valid longest increasing
             subsequence, this allows us to improve upon the exisiting soln if a longest increasing 
             subsequence starts with 2 
             tails[0] will always store the smallest value observed till index i that can be part of 
             a increasing subsequence
             tails[1] will store the second smallest value and so on
i=3 -> [2,8,9]
i=4 -> [2,8,9,10]
so length is 4 lis_length = 4

In brute force approach we are trying to store all subseqences of length 1 to length lis_length
and counting total subsequences of lis_length

we created a 2d array dp which gives for length l what are possible subsequences untill index i
we are using a List[List[List[List[int]]]]
**Brute-Force DP Enumeration**: Once we know `lis_length`, we build a
    4D DP structure `dp[length][i]`:
      - **Dimensions**: `dp` is declared as `List[List[List[List[int]]]]`, i.e.,
        `dp[length][end_idx]` is itself a **list of lists of ints**.
      - **Outer list** at `dp[length][end_idx]` collects *all* distinct increasing
        subsequences of size `length` that end precisely at index `end_idx`.
      - **Inner lists** are each one subsequence (e.g. `[3, 5, 9]`, `[3, 8, 9]`, ...).
      - We iterate from `length=2` to `lis_length`, extending every subsequence in
        `dp[length-1][prev_idx]` (for `prev_idx < end_idx`) when its last value
        is < `nums[end_idx]`.

    This explicit storage of *every* subsequence is why memory/time blow up
    exponentially (≈ sum of binomial(n, k)), since `dp[length][i]` must accommodate
    zero, one, or many subsequence lists.


    # Example (n=6): nums = [3, 1, 2, 4, 6, 5]
    # -----------------------------------------
    # dp[1]: subsequences of length 1 at each index
    #   dp[1][0] = [[3]]  # only [3] ends at index 0
    #   dp[1][1] = [[1]]
    #   dp[1][2] = [[2]]
    #   dp[1][3] = [[4]]
    #   dp[1][4] = [[6]]
    #   dp[1][5] = [[5]]
    #
    # dp[2]: subsequences of length 2
    #   dp[2][0] = []
    #   dp[2][1] = []
    #   dp[2][2] = [[1, 2]]            # from dp[1][1]
    #   dp[2][3] = [[3, 4], [1, 4], [2, 4]]
    #   dp[2][4] = [[3, 6], [1, 6], [2, 6], [4, 6]]
    #   dp[2][5] = [[3, 5], [1, 5], [2, 5], [4, 5]]
    #
    # dp[3]: subsequences of length 3
    #   dp[3][0] = []
    #   dp[3][1] = []
    #   dp[3][2] = []                  # too few elements before index 2
    #   dp[3][3] = [[1, 2, 4]]         # extending [1,2] at dp[2][2]
    #   dp[3][4] = [[1, 2, 6], [3, 4, 6], [1, 4, 6], [2, 4, 6]] # Using dp[2][2], dp[2][3]
    #   dp[3][5] = [[1, 2, 5], [3, 4, 5], [1, 4, 5], [2, 4, 5]] # using dp[2][2],dp[2][3],dp[2][4]
    #
    # dp[4]: subsequences of length 4
    #   dp[4][3] = []             
    #   dp[4][4] = [[1, 2, 4, 6]] # etc. depending on valid extensions
    #   dp[4][5] = [[1, 2, 4, 5]] # Using dp[3][3] and dp[3][4]
    #
    # Above, each dp[l][i] is a **list of lists**: the outer list groups multiple
    # subsequences, and each inner list is one full sequence.
So for each length we are iterating through length-1 index (minimum possible index that can have 
that length so length = 3 => index 2 to n 0,1,2 indexes can form a subsequence) 
So outer two loops take O(n**2)
# Build subsequences of length 2 to lis_length
    for length in range(2, lis_length + 1): O(n)
        for end_idx in range(length - 1, n): O(n)
            current_value = nums[end_idx]

"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Compute the number of longest increasing subsequences (LIS) in the list.
        This uses patience sorting to determine the LIS length and dynamic programming
        to count all subsequences of that length.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Phase 1: Determine the length of the LIS using patience sorting
        lis_tails: List[int] = [nums[0]]
        for num in nums[1:]:
            position = bisect_left(lis_tails, num)
            if position == len(lis_tails):
                lis_tails.append(num)
            else:
                lis_tails[position] = num

        lis_length = len(lis_tails)

        # If the LIS is length 1, every element is itself an LIS
        if lis_length == 1:
            return n

        # Phase 2: Build DP table where dp[length][i] holds list of subsequences
        # of 'length' ending at index i
        dp: List[List[List[List[int]]]] = [
            [[] for _ in range(n)]
            for _ in range(lis_length + 1)
        ]

        # Subsequences of length 1 are just the individual elements
        for index, value in enumerate(nums):
            dp[1][index].append([value])

        # Build subsequences of length 2 to lis_length
        for length in range(2, lis_length + 1):
            for end_idx in range(length - 1, n):
                current_value = nums[end_idx]
                # Consider all subsequences of length-1 ending before end_idx
                for prev_idx in range(length - 1, end_idx):
                    for subseq in dp[length - 1][prev_idx]:
                        if subseq[-1] < current_value:
                            # Append the new value to form a subsequence of 'length'
                            dp[length][end_idx].append(subseq + [current_value])

        # Sum up all subsequences of maximum length
        total_count = 0
        for subseq_list in dp[lis_length]:
            total_count += len(subseq_list)

        return total_count
