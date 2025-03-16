from coverage_pre_commit.common.enums.__better_enum import __BetterStrEnum


class Providers(__BetterStrEnum):
	"""
	Enum for `coverage` providers.
	"""

	UNITTEST = "unittest"
	PYTEST = "pytest"
	TOX = "tox"
