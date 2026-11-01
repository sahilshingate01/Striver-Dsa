"""
Problem: Find the row with maximum number of 1's
Difficulty: Medium
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/find-row-with-maximum-1's
Resource: https://youtu.be/SCz-1TtYxDI
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 3 : BS on 2D Arrays

Sample Input: matrix = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
Sample Output: 2
Explanation: Row 2 has 4 ones, which is the maximum.
"""


def row_with_max_1s(matrix: list[list[int]]) -> int:
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
        run_tests(__file__, row_with_max_1s)
    else:
        # Normal run with sample input
        sample_matrix = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
        print(f"Sample Input: matrix = {sample_matrix}")
        result = row_with_max_1s(sample_matrix)
        print(f"Your Output: {result}")
