"""
Problem: Split array - Largest Sum
Difficulty: Hard
Platform: leetcode
Problem Link: https://leetcode.com/problems/split-array-largest-sum
Resource: https://www.youtube.com/watch?v=thUd_WJn6wk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=20
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: nums = [7, 2, 5, 10, 8], k = 2
Sample Output: 18
Explanation: Split into [7, 2, 5] and [10, 8]. The largest sum among the two is 18.
"""


def split_array(nums: list[int], k: int) -> int:
    # TODO: Write your solution here
    return 0


# Set test_case = True to run test cases & edge cases
# Set test_case = False to run normal execution with sample input
test_case = False

if __name__ == "__main__":
    if test_case:
        import os, sys
        root = os.path.dirname(__file__)
        while root and not os.path.exists(os.path.join(root, "tests")):
            parent = os.path.dirname(root)
            if parent == root:
                break
            root = parent
        if root and root not in sys.path:
            sys.path.insert(0, root)

        from tests.runner import run_tests
        run_tests(__file__, split_array)
    else:
        # Normal run with sample input
        sample_nums = [7, 2, 5, 10, 8]
        sample_k = 2
        print(f"Sample Input: nums = {sample_nums}, k = {sample_k}")
        result = split_array(sample_nums, sample_k)
        print(f"Your Output: {result}")
