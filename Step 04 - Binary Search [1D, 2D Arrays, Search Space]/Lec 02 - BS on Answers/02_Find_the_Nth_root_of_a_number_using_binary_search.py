"""
Problem: Find the Nth root of a number using binary search
Difficulty: Medium
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/find-nth-root-of-a-number
Resource: https://youtu.be/rjEJeYCasHs
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: n = 3, m = 27
Sample Output: 3
Explanation: 3^3 = 27.
"""


def nth_root(n: int, m: int) -> int:
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
        run_tests(__file__, nth_root)
    else:
        # Normal run with sample input
        sample_n = 3
        sample_m = 27
        print(f"Sample Input: n = {sample_n}, m = {sample_m}")
        result = nth_root(sample_n, sample_m)
        print(f"Your Output: {result}")
