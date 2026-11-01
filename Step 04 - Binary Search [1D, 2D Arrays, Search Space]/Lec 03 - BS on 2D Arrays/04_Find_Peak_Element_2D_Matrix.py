"""
Problem: Find Peak Element (2D Matrix)
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/find-a-peak-element-ii
Resource: https://youtu.be/nGGp5XBzC4g?si=WCop5C6Azj5gAELH
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 3 : BS on 2D Arrays

Sample Input: mat = [[1, 4], [3, 2]]
Sample Output: [0, 1]
Explanation: 4 is strictly greater than its neighbors (1 and 2).
"""


def find_peak_grid(mat: list[list[int]]) -> list[int]:
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
        run_tests(__file__, find_peak_grid)
    else:
        # Normal run with sample input
        sample_mat = [[1, 4], [3, 2]]
        print(f"Sample Input: mat = {sample_mat}")
        result = find_peak_grid(sample_mat)
        print(f"Your Output: {result}")
