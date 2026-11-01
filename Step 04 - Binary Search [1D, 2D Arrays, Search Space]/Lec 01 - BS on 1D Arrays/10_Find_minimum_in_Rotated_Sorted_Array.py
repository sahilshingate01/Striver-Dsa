"""
Problem: Find minimum in Rotated Sorted Array
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Resource: https://youtu.be/nhEMDKMB44g
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: nums = [3, 4, 5, 1, 2]
Sample Output: 1
Explanation: Original sorted array was [1, 2, 3, 4, 5] rotated 3 times. Minimum element is 1.
"""


def find_min(nums: list[int]) -> int:
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
        run_tests(__file__, find_min)
    else:
        # Normal run with sample input
        sample_nums = [3, 4, 5, 1, 2]
        print(f"Sample Input: nums = {sample_nums}")
        result = find_min(sample_nums)
        print(f"Your Output: {result}")
