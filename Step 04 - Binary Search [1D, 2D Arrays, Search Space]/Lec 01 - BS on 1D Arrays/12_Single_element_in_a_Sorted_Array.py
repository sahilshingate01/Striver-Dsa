"""
Problem: Single element in a Sorted Array
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/single-element-in-a-sorted-array
Resource: https://youtu.be/AZOmHuHadxQ
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
Sample Output: 2
Explanation: 2 appears only once.
"""


def single_non_duplicate(nums: list[int]) -> int:
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
        run_tests(__file__, single_non_duplicate)
    else:
        # Normal run with sample input
        sample_nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        print(f"Sample Input: nums = {sample_nums}")
        result = single_non_duplicate(sample_nums)
        print(f"Your Output: {result}")
