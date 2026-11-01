"""
Problem: Find peak element
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/find-peak-element
Resource: https://youtu.be/cXxmbemS6XM
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: nums = [1, 2, 3, 1]
Sample Output: 2
Explanation: 3 is a peak element at index 2 (strictly greater than neighbors 2 and 1).
"""


def find_peak_element(nums: list[int]) -> int:
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
        run_tests(__file__, find_peak_element)
    else:
        # Normal run with sample input
        sample_nums = [1, 2, 3, 1]
        print(f"Sample Input: nums = {sample_nums}")
        result = find_peak_element(sample_nums)
        print(f"Your Output: {result}")
