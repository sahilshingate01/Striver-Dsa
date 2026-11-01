import os
import sys

def run_tests(file_path: str, func) -> bool:
    """Run all registered test cases and edge cases for the given problem file."""
    filename = os.path.basename(file_path)
    from tests.registry import get_tests_for_file

    test_data = get_tests_for_file(filename)
    if not test_data:
        print(f"No test cases registered for: {filename}")
        return False

    test_cases = test_data.get("test_cases", [])
    float_compare = test_data.get("float_compare", False)
    custom_check = test_data.get("custom_check", False)

    print(f"--- Running Test Cases for: {test_data.get('title', filename)} ---")
    passed = 0
    for i, (args, expected, desc) in enumerate(test_cases, 1):
        try:
            actual = func(*args)
            if float_compare:
                match = actual is not None and abs(actual - expected) < 1e-4
            elif custom_check:
                match = actual == expected or (isinstance(expected, list) and actual in expected)
            else:
                match = actual == expected

            if match:
                print(f"Test {i} [{desc}]: PASS")
                passed += 1
            else:
                print(f"Test {i} [{desc}]: FAIL (Expected {expected!r}, got {actual!r})")
        except Exception as e:
            print(f"Test {i} [{desc}]: ERROR ({e})")

    total = len(test_cases)
    print(f"\nResult: {passed}/{total} test cases passed.")
    return passed == total

