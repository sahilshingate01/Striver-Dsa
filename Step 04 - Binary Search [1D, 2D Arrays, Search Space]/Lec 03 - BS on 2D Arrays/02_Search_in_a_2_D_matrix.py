"""
Problem: Search in a 2 D matrix
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/search-a-2d-matrix
Resource: https://youtu.be/JXU4Akft7yk
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 3 : BS on 2D Arrays

Sample Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
Sample Output: True
Explanation: 3 is present in the matrix at matrix[0][1].
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # TODO: Write your solution here
    return False


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
        run_tests(__file__, search_matrix)
    else:
        # Normal run with sample input
        sample_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        sample_target = 3
        print(f"Sample Input: matrix = {sample_matrix}, target = {sample_target}")
        result = search_matrix(sample_matrix, sample_target)
        print(f"Your Output: {result}")
