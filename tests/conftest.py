import os
from unittest import mock

import pytest


@pytest.fixture(autouse=True)
def mock_setup_cfg():
	"""
	Mock the setup.cfg file for all tests to avoid reading the actual file.
	"""
	mock_config = """
[metadata]
name = coverage-pre-commit
version = 0.1.0
description = A pre-commit hook to run coverage on your code.
"""

	with mock.patch("builtins.open", mock.mock_open(read_data=mock_config)):
		yield


@pytest.fixture
def temp_directory(tmp_path):
	"""
	Create a temporary directory for test files.
	"""
	old_dir = os.getcwd()
	os.chdir(tmp_path)

	# Create a minimal setup.cfg file
	with open("setup.cfg", "w") as f:
		f.write("""
[metadata]
name = coverage-pre-commit
version = 0.1.0
description = A pre-commit hook to run coverage on your code.
""")

	yield tmp_path

	os.chdir(old_dir)


def pytest_addoption(parser):
	parser.addoption(
		"--run-slow",
		action="store_true",
		default=False,
		help="run slow tests",
	)


def pytest_configure(config):
	config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
	if not config.getoption("--run-slow"):
		skip_slow = pytest.mark.skip(reason="need --run-slow option to run")
		for item in items:
			if "slow" in item.keywords:
				item.add_marker(skip_slow)
