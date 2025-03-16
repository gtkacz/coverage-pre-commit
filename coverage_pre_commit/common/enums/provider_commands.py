from coverage_pre_commit.common.enums import Providers
from coverage_pre_commit.common.enums.__better_enum import __BetterStrEnum


class ProviderCommands(__BetterStrEnum, prefix="coverage run "):
	"""
	Enum for `coverage` commands for different providers.
	"""

	UNITTEST = "UNITTEST"
	PYTEST = "PYTEST"
	TOX = "TOX"


# TODO: Move these to tests
assert ProviderCommands.names == Providers.names
