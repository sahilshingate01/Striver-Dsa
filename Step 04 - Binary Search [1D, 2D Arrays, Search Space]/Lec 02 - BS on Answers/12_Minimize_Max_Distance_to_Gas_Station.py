"""
Problem: Minimize Max Distance to Gas Station
Difficulty: Hard
Platform: leetcode
Problem Link: https://leetcode.com/problems/minimize-max-distance-to-gas-station
Resource: https://www.youtube.com/watch?v=kMSBvlZ-_HA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=21
Topic: Step 4 : Binary Search [1D, 2D Arrays, Search Space]
SubTopic / Level: Lec 2 : BS on Answers

Sample Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 9
Sample Output: 0.5
Explanation: Add 1 gas station between each adjacent pair. Max distance is 0.5.
"""


def min_max_gas_dist(stations: list[int], k: int) -> float:
    # TODO: Write your solution here
    return 0.0


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
        run_tests(__file__, min_max_gas_dist)
    else:
        # Normal run with sample input
        sample_stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sample_k = 9
        print(f"Sample Input: stations = {sample_stations}, k = {sample_k}")
        result = min_max_gas_dist(sample_stations, sample_k)
        print(f"Your Output: {result}")
