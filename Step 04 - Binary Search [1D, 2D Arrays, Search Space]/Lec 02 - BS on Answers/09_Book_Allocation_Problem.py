"""
Problem: Book Allocation Problem
Difficulty: Medium
Platform: tuf
Problem Link: https://takeuforward.org/practice/dsa/book-allocation-problem
Resource: https://youtu.be/Z0hwjftStI4
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: arr = [12, 34, 67, 90], m = 2
Sample Output: 113
Explanation: Student 1 gets [12, 34, 67] (sum 113), Student 2 gets [90]. Maximum pages is 113.
"""


def find_pages(arr: list[int], m: int) -> int:
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
        run_tests(__file__, find_pages)
    else:
        # Normal run with sample input
        sample_arr = [12, 34, 67, 90]
        sample_m = 2
        print(f"Sample Input: arr = {sample_arr}, m = {sample_m}")
        result = find_pages(sample_arr, sample_m)
        print(f"Your Output: {result}")
