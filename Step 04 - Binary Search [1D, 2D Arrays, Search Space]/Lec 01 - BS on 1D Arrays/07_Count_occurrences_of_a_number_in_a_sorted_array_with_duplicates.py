"""
Problem: Count occurrences of a number in a sorted array with duplicates
Difficulty: Easy
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/count-occurrences-in-a-sorted-array
Resource: https://youtu.be/hjR1IYVx9lY
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: arr = [1, 1, 2, 2, 2, 2, 3], target = 2
Sample Output: 4
Explanation: 2 appears 4 times at indices 2, 3, 4, 5.
"""


def count_occurrences(arr: list[int], target: int) -> int:
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
        run_tests(__file__, count_occurrences)
    else:
        # Normal run with sample input
        sample_arr = [1, 1, 2, 2, 2, 2, 3]
        sample_target = 2
        print(f"Sample Input: arr = {sample_arr}, target = {sample_target}")
        result = count_occurrences(sample_arr, sample_target)
        print(f"Your Output: {result}")
