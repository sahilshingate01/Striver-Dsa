"""
Problem: Minimum days to make M bouquets
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets
Resource: https://youtu.be/TXAuxeYBTdg
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: bloomDay = [1, 10, 3, 10, 2], m = 3, k = 1
Sample Output: 3
Explanation: After 3 days, flowers bloomed are at indices 0, 2, 4 (values 1, 3, 2). We can make 3 bouquets of 1 flower.
"""


def min_days_bloom(bloomDay: list[int], m: int, k: int) -> int:
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
        run_tests(__file__, min_days_bloom)
    else:
        # Normal run with sample input
        sample_bloomDay = [1, 10, 3, 10, 2]
        sample_m = 3
        sample_k = 1
        print(f"Sample Input: bloomDay = {sample_bloomDay}, m = {sample_m}, k = {sample_k}")
        result = min_days_bloom(sample_bloomDay, sample_m, sample_k)
        print(f"Your Output: {result}")
