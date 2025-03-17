import sys
from unittest import mock

from coverage_pre_commit.util import (
	check_dependencies,
)


class TestDependencyChecker:
	@mock.patch("subprocess.check_output")
	@mock.patch("subprocess.check_call")
	def test_check_dependencies_already_installed(self, mock_check_call, mock_check_output):
		check_dependencies(["pytest-cov>=2.0.0"])

		mock_check_output.assert_called_once()
		mock_check_call.assert_not_called()

	@mock.patch("subprocess.check_output", side_effect=Exception("Not installed"))
	@mock.patch("subprocess.check_call")
	def test_check_dependencies_not_installed(self, mock_check_call, mock_check_output):
		check_dependencies(["pytest-cov>=2.0.0"])

		mock_check_output.assert_called_once()
		mock_check_call.assert_called_once_with(
			[sys.executable, "-m", "pip", "install", "pytest-cov>=2.0.0"],
			stdout=mock.ANY,
		)

	@mock.patch("subprocess.check_output")
	@mock.patch("subprocess.check_call")
	def test_check_dependencies_empty_list(self, mock_check_call, mock_check_output):
		check_dependencies([])

		mock_check_output.assert_not_called()
		mock_check_call.assert_not_called()
