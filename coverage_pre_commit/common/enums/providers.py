from types import MappingProxyType

from coverage_pre_commit.common.enums import BetterEnum


class Providers(BetterEnum):
	"""
	Enum for `coverage` providers.
	"""

	@staticmethod
	def __command_prefix(command: str) -> str:
		return f"coverage run {command}"

	UNITTEST = MappingProxyType({
		"name": "unittest",
		"command": __command_prefix("-m unittest"),
		"default_args": [],
		"fail_command": {
			"command": "coverage report --fail-under={}",
			"is_arg": False,
		},
		"dependencies": [],
	})
	PYTEST = MappingProxyType({
		"name": "pytest",
		"command": "pytest",
		"default_args": ["--cov=.", "tests/"],
		"fail_command": {
			"command": "--cov-fail-under={}",
			"is_arg": True,
		},
		"dependencies": ["pytest-cov~=6.0.0"],
	})
