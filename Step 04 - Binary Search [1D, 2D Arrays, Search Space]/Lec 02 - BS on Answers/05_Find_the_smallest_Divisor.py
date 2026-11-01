"""
Problem: Find the smallest Divisor
Difficulty: Medium
Platform: leetcode
Problem Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
Resource: https://youtu.be/UvBKTVaG6U8
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: nums = [1, 2, 5, 9], threshold = 6
Sample Output: 5
Explanation: If divisor is 5: ceil(1/5)+ceil(2/5)+ceil(5/5)+ceil(9/5) = 1+1+1+2 = 5 <= 6.
"""


def smallest_divisor(nums: list[int], threshold: int) -> int:
    # TODO: Write your solution here
    return 1


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
        run_tests(__file__, smallest_divisor)
    else:
        # Normal run with sample input
        sample_nums = [1, 2, 5, 9]
        sample_threshold = 6
        print(f"Sample Input: nums = {sample_nums}, threshold = {sample_threshold}")
        result = smallest_divisor(sample_nums, sample_threshold)
        print(f"Your Output: {result}")
