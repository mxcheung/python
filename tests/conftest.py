"""Test configuration to ensure the project package is importable during tests.

This makes the repository root available on sys.path so `from hello.hello import ...` works
regardless of the current working directory when pytest is invoked.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
