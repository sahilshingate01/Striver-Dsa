"""
Problem: Kth element of 2 sorted arrays
Difficulty: Medium
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/kth-element-of-2-sorted-arrays
Resource: https://youtu.be/D1oDwWCq50g
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
Sample Output: 6
Explanation: Merged sorted array = [1, 2, 3, 4, 6, 7, 8, 9, 10]. 5th element is 6.
"""


def kth_element(a: list[int], b: list[int], k: int) -> int:
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
        run_tests(__file__, kth_element)
    else:
        # Normal run with sample input
        sample_a = [2, 3, 6, 7, 9]
        sample_b = [1, 4, 8, 10]
        sample_k = 5
        print(f"Sample Input: a = {sample_a}, b = {sample_b}, k = {sample_k}")
        result = kth_element(sample_a, sample_b, sample_k)
        print(f"Your Output: {result}")
