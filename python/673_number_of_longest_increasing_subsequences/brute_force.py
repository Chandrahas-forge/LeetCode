from bisect import bisect_left
from typing import List
"""
Phase 1 — Determining LIS length using lis_tails
------------------------------------------------
We maintain `lis_tails` such that:
    lis_tails[j] stores the smallest possible tail value of any increasing
    subsequence of length j+1 seen so far (up to the current index).

Example: nums = [7, 8, 2, 9, 10]

i = 0 → lis_tails = [7]
i = 1 → lis_tails = [7, 8]
    - 7 and 8 are the smallest possible values forming an increasing subsequence of lengths 1 and 2.

i = 2 → lis_tails = [2, 8]
    - Replace 7 with 2. Even though 2 is not in the final LIS,
      keeping the tail minimal allows potentially longer subsequences later.
    - General rule:
        lis_tails[0] is always the smallest starting value possible.
        lis_tails[1] is the smallest feasible second value, and so on.

i = 3 → lis_tails = [2, 8, 9]
i = 4 → lis_tails = [2, 8, 9, 10]

So the LIS length is 4.
------------------------------------------------
Phase 2 — Explicit Enumeration of All Increasing Subsequences of Each Length
---------------------------------------------------------------------------
Once we know `lis_length`, we enumerate all increasing subsequences (not just count them)
using a 2D structure:

    subseqs[length][end_idx]  is a list of subsequences (each is a List[int])
    of size `length` that end exactly at index `end_idx`.

Meaning:
    • The first dimension selects the subsequence length.
    • The second dimension selects where the subsequence ends in the array.
    • Each stored entry is a full subsequence, not just a count or state.

Type:
    subseqs: List[List[List[List[int]]]]


Initialization (base subsequences of length 1):
    subseqs[1][i] = [[nums[i]]]  for all i in 0..n-1


Extension Rule (build lengths 2..lis_length):
    For length from 2 to lis_length:

        The subsequences of size (length-1) must end at some index ≥ (length-2).
        This is because a subsequence of size k requires at least k elements,
        so its earliest possible ending index is (k-1).

        Thus the earliest valid end index for a (length-1)-subsequence is:
            prev_end_idx >= length - 2

        For each possible ending position of the new subsequence:
            for end_idx in range(length - 1, n):
                current_value = nums[end_idx]

                We extend *all* (length-1)-subsequences that end earlier:
                    for prev_end_idx in range(length - 2, end_idx):

                        And for each such subsequence:
                            for s in subseqs[length - 1][prev_end_idx]:

                                We can only extend if the values remain increasing:
                                    if s[-1] < current_value:
                                        subseqs[length][end_idx].append(s + [current_value])


Result (final count):
    number_of_LIS = sum(len(subseqs[lis_length][i]) for i in range(n))


Why the index bounds matter:
    • prev_end_idx < end_idx
        - The previous subsequence must use strictly earlier indices,
          otherwise the sequence would not be strictly increasing in index order.

    • prev_end_idx >= (length - 2)
        - A subsequence of size (length-1) cannot end earlier than (length-2),
          so anything before that is guaranteed empty and can be skipped.

    • end_idx >= (length - 1)
        - A subsequence of size `length` must occupy at least `length` positions.


Worked Example (nums = [3, 1, 2, 4, 6, 5]):
--------------------------------------------

subseqs[1]:
    [3], [1], [2], [4], [6], [5]

subseqs[2] (extend length-1 subsequences):
    subseqs[2][2] = [[1, 2]]
        - extend [1] → [1,2]
        - [3] cannot extend because 3 > 2

    subseqs[2][3] = [[3,4], [1,4], [2,4]]
    subseqs[2][4] = [[3,6], [1,6], [2,6], [4,6]]
    subseqs[2][5] = [[3,5], [1,5], [2,5], [4,5]]

subseqs[3]:
    subseqs[3][3] = [[1, 2, 4]]
    subseqs[3][4] = [[1, 2, 6], [3, 4, 6], [1, 4, 6], [2, 4, 6]]
    subseqs[3][5] = [[1, 2, 5], [3, 4, 5], [1, 4, 5], [2, 4, 5]]

subseqs[4]:
    subseqs[4][4] = [[1, 2, 4, 6]]
    subseqs[4][5] = [[1, 2, 4, 5]]

(Each subseqs[length][i] is a full set of all increasing subsequences of that length that end at index i.)
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # -------------------------
        # Phase 1: Compute LIS length using patience sorting
        # -------------------------
        lis_tails: List[int] = []
        for x in nums:
            pos = bisect_left(lis_tails, x)
            if pos == len(lis_tails):
                lis_tails.append(x)
            else:
                lis_tails[pos] = x

        lis_length = len(lis_tails)

        # Special case: if LIS length is 1 → every single element is an LIS
        if lis_length == 1:
            return n

        # --------------------------------------------------------
        # Phase 2: Explicit enumeration of LIS-length subsequences
        #
        # subseqs[length][end_idx] = list of *all increasing subsequences*
        # of size `length` that end exactly at index `end_idx`.
        #
        # Example:
        #   subseqs[2][5] = [[3,5], [1,5], [2,5], [4,5]]
        #
        # NOTE: This stores ALL subsequences (not counts), so memory/time
        #       blow up is combinatorial in worst cases.
        # --------------------------------------------------------
        subseqs: List[List[List[List[int]]]] = [
            [[] for _ in range(n)] for _ in range(lis_length + 1)
        ]

        # Base case: length-1 subsequences are just each individual element.
        for i, v in enumerate(nums):
            subseqs[1][i].append([v])

        # --------------------------------------------------------
        # Build subsequences of length 2 up to lis_length
        # --------------------------------------------------------
        for length in range(2, lis_length + 1):

            # The shortest index where a subsequence of length (length-1)
            # can possibly end is (length-2).
            #
            # Example:
            #   If we are building length=3 subsequences,
            #   then length-1 = 2 → earliest end index = 1.
            #
            # Starting earlier would check indices where subseqs[length-1][i] is empty.
            prev_end_start = length - 2

            # Now choose where the new length-`length` subsequence ends.
            # A subsequence of size `length` must use at least `length` elements,
            # so the earliest valid end_idx is (length-1).
            for end_idx in range(length - 1, n):
                current_value = nums[end_idx]

                # We now look for *length-1* subsequences that end before `end_idx`.
                # They must end at some index prev_end_idx < end_idx,
                # and prev_end_idx must be >= prev_end_start (otherwise they cannot exist).
                for prev_end_idx in range(prev_end_start, end_idx):

                    # Try to extend each subsequence of length-1 ending at prev_end_idx.
                    for subseq in subseqs[length - 1][prev_end_idx]:

                        # Increasing subsequence rule: last value < new appended value
                        if subseq[-1] < current_value:
                            # Form a new length-`length` subsequence ending at end_idx
                            subseqs[length][end_idx].append(subseq + [current_value])

        # --------------------------------------------------------
        # The LIS count is the number of subsequences of length = lis_length
        # across all ending indices.
        # --------------------------------------------------------
        total_count = sum(len(subseq_list) for subseq_list in subseqs[lis_length])
        return total_count
