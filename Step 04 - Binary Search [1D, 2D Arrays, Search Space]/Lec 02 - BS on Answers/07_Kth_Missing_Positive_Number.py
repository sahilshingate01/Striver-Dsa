"""
Problem: Kth Missing Positive Number
Difficulty: Easy
Platform: leetcode
Problem Link: https://leetcode.com/problems/kth-missing-positive-number
Resource: https://youtu.be/uZ0N_hZpyps
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: arr = [2, 3, 4, 7, 11], k = 5
Sample Output: 9
Explanation: Missing numbers are [1, 5, 6, 8, 9, 10, ...]. The 5th missing is 9.
"""


def find_kth_positive(arr: list[int], k: int) -> int:
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
        run_tests(__file__, find_kth_positive)
    else:
        # Normal run with sample input
        sample_arr = [2, 3, 4, 7, 11]
        sample_k = 5
        print(f"Sample Input: arr = {sample_arr}, k = {sample_k}")
        result = find_kth_positive(sample_arr, sample_k)
        print(f"Your Output: {result}")
