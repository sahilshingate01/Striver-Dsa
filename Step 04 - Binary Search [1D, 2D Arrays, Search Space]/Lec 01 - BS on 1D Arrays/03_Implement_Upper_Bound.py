"""
Problem: Implement Upper Bound
Difficulty: Easy
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/upper-bound
Resource: https://youtu.be/6zhGS79oQ4k
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: arr = [2, 3, 6, 7, 8, 8, 11, 11, 12], target = 6
Sample Output: 3
Explanation: Smallest element strictly > 6 is 7 at index 3.
"""


def upper_bound(arr: list[int], target: int) -> int:
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
        run_tests(__file__, upper_bound)
    else:
        # Normal run with sample input
        sample_arr = [2, 3, 6, 7, 8, 8, 11, 11, 12]
        sample_target = 6
        print(f"Sample Input: arr = {sample_arr}, target = {sample_target}")
        result = upper_bound(sample_arr, sample_target)
        print(f"Your Output: {result}")
