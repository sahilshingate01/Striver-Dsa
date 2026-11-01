"""
Problem: Matrix Median
Difficulty: Hard
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/matrix-median
Resource: https://youtu.be/Q9wXgdxJq48?si=ScI_0uzJh7yg8nrX
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 3 : BS on 2D Arrays

Sample Input: matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
Sample Output: 5
Explanation: Sorted elements are [1, 2, 3, 3, 5, 6, 6, 9, 9]. Median is 5.
"""


def matrix_median(matrix: list[list[int]]) -> int:
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
        run_tests(__file__, matrix_median)
    else:
        # Normal run with sample input
        sample_matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
        print(f"Sample Input: matrix = {sample_matrix}")
        result = matrix_median(sample_matrix)
        print(f"Your Output: {result}")
