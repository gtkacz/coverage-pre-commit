from unittest import mock

import pytest

from coverage_pre_commit.coverage_runner import main
from coverage_pre_commit.util import (
	EMPTY_NAMESPACE,
)


class TestCoverageRunner:
	@mock.patch("sys.exit")
	@mock.patch("coverage_pre_commit.coverage_runner.get_metadata")
	def test_main_version_flag(self, mock_get_metadata, mock_exit):
		mock_get_metadata.return_value = "0.1.0"
		with mock.patch("sys.stdout", new=mock.MagicMock()):
			main(["--version"])

		mock_get_metadata.assert_called_once_with("version")
		mock_exit.assert_called_once_with(0)

	@mock.patch("sys.exit")
	@mock.patch("argparse.ArgumentParser.print_help")
	def test_main_empty_args(self, mock_print_help, mock_exit):
		with mock.patch("argparse.ArgumentParser.parse_args") as mock_parse_args:
			mock_parse_args.return_value = EMPTY_NAMESPACE
			main([])

		mock_print_help.assert_called_once()
		mock_exit.assert_called_once_with(0)

	@mock.patch("sys.exit")
	def test_main_no_fail_under(self, mock_exit):
		with pytest.raises(RuntimeError) as excinfo:
			main(["--provider", "unittest"])

		assert "fail-under argument must be passed" in str(excinfo.value)

	@mock.patch("sys.exit")
	def test_main_invalid_fail_under_high(self, mock_exit):
		with pytest.raises(RuntimeError) as excinfo:
			main(["--provider", "unittest", "--fail-under", "101"])

		assert "fail-under argument must be passed and must be between 0 and 100" in str(excinfo.value)

	@mock.patch("sys.exit")
	def test_main_invalid_fail_under_low(self, mock_exit):
		with pytest.raises(RuntimeError) as excinfo:
			main(["--provider", "unittest", "--fail-under", "-1"])

		assert "fail-under argument must be passed and must be between 0 and 100" in str(excinfo.value)

	@mock.patch("sys.exit")
	def test_main_unsupported_provider_no_command(self, mock_exit):
		with pytest.raises(RuntimeError) as excinfo:
			main(["--provider", "unsupported", "--fail-under", "80"])

		assert "If you are using an unsupported provider, you must also provide a command" in str(excinfo.value)

	@mock.patch("coverage_pre_commit.coverage_runner.execute_command")
	@mock.patch("sys.exit")
	def test_main_with_custom_command(self, mock_exit, mock_execute_command):
		mock_execute_command.return_value = 0

		main(["--fail-under", "80", "--command", "custom command"])

		mock_execute_command.assert_called_once_with("custom command")
		mock_exit.assert_called_once_with(0)

	@mock.patch("coverage_pre_commit.coverage_runner.check_dependencies")
	@mock.patch("coverage_pre_commit.coverage_runner.execute_command")
	@mock.patch("sys.exit")
	def test_main_with_extra_dependencies(self, mock_exit, mock_execute_command, mock_check_dependencies):
		mock_execute_command.return_value = 0

		main(["--fail-under", "80", "--provider", "unittest", "--extra-dependencies", "pytest,pytest-cov"])

		mock_check_dependencies.assert_called_once_with(["pytest", "pytest-cov"])
		mock_execute_command.assert_called_once()
		mock_exit.assert_called_once_with(0)

	@mock.patch("coverage_pre_commit.coverage_runner.check_dependencies")
	@mock.patch("coverage_pre_commit.coverage_runner.build_command")
	@mock.patch("coverage_pre_commit.coverage_runner.execute_command")
	@mock.patch("sys.exit")
	def test_main_with_unittest(self, mock_exit, mock_execute_command, mock_build_command, mock_check_dependencies):
		mock_build_command.return_value = "unittest command"
		mock_execute_command.return_value = 0

		main(["--fail-under", "80", "--provider", "unittest"])

		mock_check_dependencies.assert_called_once_with([])
		mock_build_command.assert_called_once()
		mock_execute_command.assert_called_once_with("unittest command")
		mock_exit.assert_called_once_with(0)

	@mock.patch("coverage_pre_commit.coverage_runner.check_dependencies")
	@mock.patch("coverage_pre_commit.coverage_runner.build_command")
	@mock.patch("coverage_pre_commit.coverage_runner.execute_command")
	@mock.patch("sys.exit")
	def test_main_with_pytest(self, mock_exit, mock_execute_command, mock_build_command, mock_check_dependencies):
		mock_build_command.return_value = "pytest command"
		mock_execute_command.return_value = 0

		main(["--fail-under", "80", "--provider", "pytest"])

		mock_check_dependencies.assert_called_once_with(["pytest-cov>=2.0.0"])
		mock_build_command.assert_called_once()
		mock_execute_command.assert_called_once_with("pytest command")
		mock_exit.assert_called_once_with(0)
