import os
import pytest
from your_module import load_file_as_bytes

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data', 'ipt')

# Discover files in data/ipt/ to use as test cases
def get_test_files():
    return [
        os.path.join(DATA_DIR, f)
        for f in os.listdir(DATA_DIR)
        if os.path.isfile(os.path.join(DATA_DIR, f))
    ]

@pytest.mark.parametrize("file_path", get_test_files())
def test_load_each_file_as_bytes(file_path):
    content = load_file_as_bytes(file_path)
    assert isinstance(content, bytes)
    assert len(content) > 0  # Optional: Ensure file is not empty
