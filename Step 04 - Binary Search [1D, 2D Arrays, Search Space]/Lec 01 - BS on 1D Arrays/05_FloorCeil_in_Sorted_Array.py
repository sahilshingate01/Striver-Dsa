"""
Problem: Floor/Ceil in Sorted Array
Difficulty: Medium
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/floor-and-ceil-in-sorted-array
Resource: https://www.youtube.com/watch?v=6zhGS79oQ4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=3
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: arr = [3, 4, 4, 7, 8, 10], target = 5
Sample Output: (4, 7)
Explanation: Floor is 4 (largest <= 5) and Ceil is 7 (smallest >= 5).
"""


def get_floor_and_ceil(arr: list[int], target: int) -> tuple[int, int]:
    # TODO: Write your solution here
    return (-1, -1)


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
        run_tests(__file__, get_floor_and_ceil)
    else:
        # Normal run with sample input
        sample_arr = [3, 4, 4, 7, 8, 10]
        sample_target = 5
        print(f"Sample Input: arr = {sample_arr}, target = {sample_target}")
        result = get_floor_and_ceil(sample_arr, sample_target)
        print(f"Your Output: {result}")
