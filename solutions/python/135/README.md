# 135. Candy

    **Difficulty:** Hard  
    **Tags:** Greedy, Array, One-Pass

    ## Problem Statement

    > There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.
    >
    > You must give candies to these children according to the rules:
    >
    > 1. Each child must have **at least one** candy.  
    > 2. Children with a **higher rating** get **more candies** than their immediate neighbours.
    >
    > Return the *minimum* number of candies you need to distribute.

    ## Examples

    | # | Input | Output | Explanation |
    |---|-------|--------|-------------|
    | 1 | `ratings = [1, 0, 2]` | `5` | Allocate `[2, 1, 2]` candies. |
    | 2 | `ratings = [1, 2, 2]` | `4` | Allocate `[1, 2, 1]`; the third child can keep only one candy because its rating is not higher than its right neighbour. |

    ## Constraints

    * `1 ≤ n ≤ 20 000`  
    * `0 ≤ ratings[i] ≤ 20 000`

    ---
