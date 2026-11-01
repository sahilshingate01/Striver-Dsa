"""
Problem: Median of 2 sorted arrays
Difficulty: Hard
Platform: leetcode
Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays
Resource: https://youtu.be/C2rRzz-JDk8
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: nums1 = [1, 3], nums2 = [2]
Sample Output: 2.0
Explanation: Merged array = [1, 2, 3], median is 2.0.
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    # TODO: Write your solution here
    return 0.0


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
        run_tests(__file__, find_median_sorted_arrays)
    else:
        # Normal run with sample input
        sample_nums1 = [1, 3]
        sample_nums2 = [2]
        print(f"Sample Input: nums1 = {sample_nums1}, nums2 = {sample_nums2}")
        result = find_median_sorted_arrays(sample_nums1, sample_nums2)
        print(f"Your Output: {result}")
