"""
Problem: Find out how many times has an array been rotated
Difficulty: Easy
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/find-out-how-many-times-the-array-is-rotated
Resource: https://youtu.be/jtSiWTPLwd0
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: arr = [5, 1, 2, 3, 4]
Sample Output: 1
Explanation: Array was rotated right by 1 position (min element 1 is at index 1).
"""


def find_rotation_count(arr: list[int]) -> int:
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
        run_tests(__file__, find_rotation_count)
    else:
        # Normal run with sample input
        sample_arr = [5, 1, 2, 3, 4]
        print(f"Sample Input: arr = {sample_arr}")
        result = find_rotation_count(sample_arr)
        print(f"Your Output: {result}")
