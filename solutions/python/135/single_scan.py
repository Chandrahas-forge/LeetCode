from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        ------------------------------------------------------------
        Overview
        ------------------------------------------------------------
        Single left-to-right sweep with two counters:

            asc : length of the current strictly-increasing run
                  that ends at ratings[ind-1].
                  The *peak* child of that run currently owns
                  exactly `asc` candies.

            des : how many steps deep we are inside the current
                  strictly-decreasing run (counted so far).

        Invariants
        ----------
        • Every child visited so far has at least one candy.
        • For an increasing run we hand out the *final* candies
          immediately (1, 2, …, asc).
        • For a decreasing run we *temporarily* hand out
          1, 2, …, des **left-to-right**, even though in the *final*
          layout those values belong **right-to-left**.
        • Reversing those candies costs nothing except at the peak
          where the two directions meet — that single child may need
          extra candies if des ≥ asc.
        • The peak is topped up by `des − asc + 1` exactly when
          des ≥ asc; otherwise it already has enough.

        Peak top-up
        -----------
            if des >= asc:
                ans += des - asc + 1

        simply performs that one correction; no candies are ever
        taken away from anyone.
        """

        ind = 1
        asc = 1        # length of the current ascending run (includes the peak)
        des = 0        # length of the current descending run counted so far
        ans = 1        # ratings[0] always gets 1 candy
        n = len(ratings)

        # AI_COMMENTARY:
        # ------------------------------------------------------------------
        # We iterate in three logical phases inside each outer-loop cycle:
        #
        #   1. **Strictly-increasing run**
        #        - Move `ind` forward while ratings rise.
        #        - Each step extends `asc` and immediately grants that many
        #          candies.  The running total `ans` is updated on the spot.
        #
        #   2. **Strictly-decreasing run**
        #        - Continue moving `ind` while ratings fall.
        #        - Assign candies 1, 2, …, `des` left-to-right.
        #          *Why is this legal?*  After the scan we conceptually flip
        #          those numbers right-to-left, which yields the proper
        #          descending sequence …, 3, 2, 1.  The only child whose
        #          candy count might then be wrong is the *peak* (because
        #          that value collides with the asc-side assignment).
        #
        #   3. **Plateau / reset**
        #        - If the next two ratings are equal, give the newcomer one
        #          candy and reset counters; otherwise simply reset counters
        #          for the next up-slope.
        #
        # The peak-correction line placed after Phase 2 fixes the only
        # potential conflict by *adding* candies, never removing them.
        # ------------------------------------------------------------------

        while ind < n:

            # ---------------------------------------------------------
            # Step 1 : Strictly-increasing run
            # ---------------------------------------------------------
            while ind < n and ratings[ind] > ratings[ind - 1]:
                asc += 1
                ans += asc
                ind += 1

            # AI_COMMENTARY:
            # The child at ratings[ind-1] is now the local peak.
            # It has been given `asc` candies.  Whether that is enough
            # depends on how far we will now descend.

            # ---------------------------------------------------------
            # Step 2 : Strictly-decreasing run
            # ---------------------------------------------------------
            while ind < n and ratings[ind] < ratings[ind - 1]:
                des += 1
                ind += 1
                ans += des

            # AI_COMMENTARY:
            # Example walk-through (ratings 3 5 7 6 5 4 3):
            #
            #   • Asc segment: 3 children → asc = 3, candies 1 2 3
            #   • Des segment: 3 children → des = 3, candies 1 2 3
            #
            #   Interim candies (L→R): 1 2 3 1 2 3
            #   If we flip the downslope to its natural direction (R→L),
            #   we want             …           3 2 1 instead.
            #   The rightmost 3 matches; the middle 2 matches; the peak
            #   must jump from 3 to 4.  That delta is `des − asc + 1`.

            # ---------------------------------------------------------
            # Step 3 : Peak correction
            # ---------------------------------------------------------
            if des >= asc:
                ans += des - asc + 1  # AI_COMMENTARY: top-up only; no removals

            # AI_COMMENTARY:
            # No further conflicts exist:
            #   • upslope already satisfied left neighbour rule,
            #   • downslope (when viewed right-to-left) satisfies
            #     right neighbour rule,
            #   • the peak now outranks both neighbours.

            if ind == n:              # All ratings processed
                return ans

            # ---------------------------------------------------------
            # Step 4 : Plateau / reset for the next segment
            # ---------------------------------------------------------
            if ratings[ind] == ratings[ind - 1]:
                # AI_COMMENTARY:
                # Equal ratings can both safely hold one candy.
                ans += 1
                asc = 1
                des = 0
                ind += 1
            else:
                # AI_COMMENTARY:
                # New ascending run will start at ratings[ind].
                asc = 1
                des = 0

        return ans


        return