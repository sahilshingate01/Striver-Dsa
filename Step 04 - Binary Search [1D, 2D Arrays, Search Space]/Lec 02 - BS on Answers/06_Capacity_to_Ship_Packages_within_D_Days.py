"""
Problem: Capacity to Ship Packages within D Days
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
Resource: https://youtu.be/MG-Ac4TAvTY
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
Sample Output: 15
Explanation: Ship capacity of 15 ships packages across 5 days: [1..5], [6,7], [8], [9], [10].
"""


def ship_within_days(weights: list[int], days: int) -> int:
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
        run_tests(__file__, ship_within_days)
    else:
        # Normal run with sample input
        sample_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sample_days = 5
        print(f"Sample Input: weights = {sample_weights}, days = {sample_days}")
        result = ship_within_days(sample_weights, sample_days)
        print(f"Your Output: {result}")
