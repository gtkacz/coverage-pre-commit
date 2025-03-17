import os
import sys
from unittest import mock

import pytest

from coverage_pre_commit.coverage_runner import main


@pytest.fixture
def mock_subprocess_run():
	with mock.patch("subprocess.run") as mock_run:
		process_mock = mock.MagicMock()
		process_mock.check_returncode.return_value = 0
		mock_run.return_value = process_mock
		yield mock_run


@pytest.fixture
def mock_dependencies():
	with mock.patch("coverage_pre_commit.coverage_runner.check_dependencies") as mock_check:
		yield mock_check


class TestIntegration:
	def test_unittest_integration(self, mock_subprocess_run, mock_dependencies):
		# Setup test with valid arguments
		test_args = ["--provider", "unittest", "--fail-under", "80"]

		# Run the main function with test arguments
		with mock.patch("sys.exit") as mock_exit:
			main(test_args)

		# Verify dependencies were checked
		mock_dependencies.assert_called_once()

		# Verify correct command was executed
		mock_subprocess_run.assert_called_once()
		args, kwargs = mock_subprocess_run.call_args
		assert kwargs["shell"] is True
		command = args[0]
		assert "coverage run -m unittest" in command
		assert "coverage report --fail-under=80" in command

		# Verify exit code was correct
		mock_exit.assert_called_once_with(0)

	def test_pytest_integration(self, mock_subprocess_run, mock_dependencies):
		# Setup test with valid arguments
		test_args = ["--provider", "pytest", "--fail-under", "90", "--args", "--verbose"]

		# Run the main function with test arguments
		with mock.patch("sys.exit") as mock_exit:
			main(test_args)

		# Verify dependencies were checked
		mock_dependencies.assert_called()

		# Verify correct command was executed
		mock_subprocess_run.assert_called_once()
		args, kwargs = mock_subprocess_run.call_args
		assert kwargs["shell"] is True
		command = args[0]
		assert "pytest" in command
		assert "--cov=." in command
		assert "tests/" in command
		assert "--verbose" in command
		assert "--cov-fail-under=90" in command

		# Verify exit code was correct
		mock_exit.assert_called_once_with(0)

	def test_custom_command_integration(self, mock_subprocess_run, mock_dependencies):
		# Setup test with custom command
		test_args = [
			"--fail-under",
			"85",
			"--command",
			"python -m pytest --cov=src/ tests/ --cov-fail-under=85",
		]

		# Run the main function with test arguments
		with mock.patch("sys.exit") as mock_exit:
			main(test_args)

		# Verify correct command was executed
		mock_subprocess_run.assert_called_once()
		args, kwargs = mock_subprocess_run.call_args
		assert kwargs["shell"] is True
		command = args[0]
		assert command == "python -m pytest --cov=src/ tests/ --cov-fail-under=85"

		# Verify exit code was correct
		mock_exit.assert_called_once_with(0)

	def test_extra_dependencies_integration(self, mock_subprocess_run, mock_dependencies):
		# Setup test with extra dependencies
		test_args = [
			"--provider",
			"unittest",
			"--fail-under",
			"80",
			"--extra-dependencies",
			"pytest-cov,pytest-xdist",
		]

		# Run the main function with test arguments
		with mock.patch("sys.exit") as mock_exit:
			main(test_args)

		# Verify dependencies were checked
		mock_dependencies.assert_any_call(["pytest-cov", "pytest-xdist"])

		# Verify correct command was executed
		mock_subprocess_run.assert_called_once()

		# Verify exit code was correct
		mock_exit.assert_called_once_with(0)


@pytest.mark.parametrize(
	"test_args,expected_error",
	[
		(
			["--provider", "unknown", "--fail-under", "80"],
			"If you are using an unsupported provider, you must also provide a command",
		),
		(
			["--provider", "unittest", "--fail-under", "101"],
			"The fail-under argument must be passed and must be between 0 and 100",
		),
		(
			["--provider", "unittest", "--fail-under", "-1"],
			"The fail-under argument must be passed and must be between 0 and 100",
		),
		(
			["--provider", "unittest"],
			"The fail-under argument must be passed",
		),
	],
)
def test_error_cases(test_args, expected_error):
	with pytest.raises(RuntimeError) as excinfo:
		main(test_args)

	assert expected_error in str(excinfo.value)


@pytest.mark.skipif(sys.platform == "win32", reason="Different command behavior on Windows")
class TestWithRealSubprocess:
	"""Tests that run real subprocesses (should be skipped in CI environments)"""

	@mock.patch("sys.exit")
	def test_execute_command_real(self, mock_exit):
		with pytest.MonkeyPatch.context() as mp:
			# Create a temporary test script
			script_content = "print('Test successful')"
			script_path = "temp_test_script.py"

			try:
				with open(script_path, "w") as f:
					f.write(script_content)

				# Run the main function with a real command
				main([
					"--fail-under",
					"100",
					"--command",
					f"{sys.executable} {script_path}",
				])

				# Verify exit was called
				mock_exit.assert_called_once()
			finally:
				# Clean up
				if os.path.exists(script_path):
					os.remove(script_path)
