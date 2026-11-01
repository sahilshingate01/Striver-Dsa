"""
Problem: Search in Rotated Sorted Array I
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array
Resource: https://youtu.be/5qGrJbHhqFs
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Sample Output: 4
Explanation: 0 is found at index 4.
"""


def search(nums: list[int], target: int) -> int:
    # TODO: Write your solution here
    return -1


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
        run_tests(__file__, search)
    else:
        # Normal run with sample input
        sample_nums = [4, 5, 6, 7, 0, 1, 2]
        sample_target = 0
        print(f"Sample Input: nums = {sample_nums}, target = {sample_target}")
        result = search(sample_nums, sample_target)
        print(f"Your Output: {result}")
