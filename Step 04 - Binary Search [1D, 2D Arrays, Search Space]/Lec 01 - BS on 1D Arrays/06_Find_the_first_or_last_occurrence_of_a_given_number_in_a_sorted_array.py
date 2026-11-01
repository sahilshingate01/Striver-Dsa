"""
Problem: Find the first or last occurrence of a given number in a sorted array
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
Resource: https://youtu.be/hjR1IYVx9lY
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Sample Output: [3, 4]
Explanation: First occurrence of 8 is index 3, last occurrence is index 4.
"""


def search_range(nums: list[int], target: int) -> list[int]:
    # TODO: Write your solution here
    return [-1, -1]


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
        run_tests(__file__, search_range)
    else:
        # Normal run with sample input
        sample_nums = [5, 7, 7, 8, 8, 10]
        sample_target = 8
        print(f"Sample Input: nums = {sample_nums}, target = {sample_target}")
        result = search_range(sample_nums, sample_target)
        print(f"Your Output: {result}")
