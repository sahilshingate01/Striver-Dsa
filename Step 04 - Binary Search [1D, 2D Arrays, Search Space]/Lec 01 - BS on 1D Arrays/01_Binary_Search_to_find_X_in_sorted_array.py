"""
Problem: Binary Search to find X in sorted array
Difficulty: Easy
Platform: leetcode
Problem Link: https://leetcode.com/problems/binary-search
Resource: https://youtu.be/MHf6awe89xw
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 1 : BS on 1D Arrays

Sample Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Sample Output: 4
Explanation: 9 exists in nums and its index is 4.
"""


def binary_search(nums: list[int], target: int) -> int:
    l = 0
    h = len(nums) - 1
    ans = -1

    while l <= h :
        mid = (l + h) // 2
        
        if nums[mid] == target :
            return mid
        
        elif target < nums[mid] :
            h = mid - 1
        
        else :
            l = mid + 1
        
    return ans

# Set test_case = True to run test cases & edge cases
# Set test_case = False to run normal execution with sample input
test_case = True

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
        run_tests(__file__, binary_search)
    else:
        # Normal run with sample input
        sample_nums = [-1, 0, 3, 5, 9, 12]
        sample_target = 9
        print(f"Sample Input: nums = {sample_nums}, target = {sample_target}")
        result = binary_search(sample_nums, sample_target)
        print(f"Your Output: {result}")
