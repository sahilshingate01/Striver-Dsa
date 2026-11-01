"""
Problem: Find square root of a number in log n
Difficulty: Easy
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/find-square-root-of-a-number
Resource: https://youtu.be/Bsv3FPUX_BA
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: n = 5
Sample Output: 2
Explanation: Square root of 5 is 2.236..., integer floor is 2.
"""


def floor_sqrt(n: int) -> int:
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
        run_tests(__file__, floor_sqrt)
    else:
        # Normal run with sample input
        sample_n = 5
        print(f"Sample Input: n = {sample_n}")
        result = floor_sqrt(sample_n)
        print(f"Your Output: {result}")
