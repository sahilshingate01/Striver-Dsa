from tests.step04_data import STEP04_TESTS

REGISTRY = {
    **STEP04_TESTS,
}

def get_tests_for_file(filename: str):
    return REGISTRY.get(filename)

