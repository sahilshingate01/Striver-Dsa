"""
Problem: Aggressive Cows
Difficulty: Hard
Platform: spoj
Problem Link: https://www.spoj.com/problems/AGGRCOW/
Resource: https://youtu.be/R_Mfw4ew-Vo
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: stalls = [0, 3, 4, 7, 10, 9], k = 4
Sample Output: 3
Explanation: Place cows at stalls [0, 3, 7, 10]. Minimum distance between any two cows is 3.
"""


def aggressive_cows(stalls: list[int], k: int) -> int:
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
        run_tests(__file__, aggressive_cows)
    else:
        # Normal run with sample input
        sample_stalls = [0, 3, 4, 7, 10, 9]
        sample_k = 4
        print(f"Sample Input: stalls = {sample_stalls}, k = {sample_k}")
        result = aggressive_cows(sample_stalls, sample_k)
        print(f"Your Output: {result}")
