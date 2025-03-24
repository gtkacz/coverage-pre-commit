from typing import TypedDict


class FailCommand(TypedDict):
	"""
	FailCommand is a typed dictionary that represents the structure of a fail command.
	"""

	command: str
	is_arg: bool


class ProviderValue(TypedDict):
	"""
	ProviderValue is a typed dictionary that represents the structure of a provider value.
	"""

	name: str
	command: str
	default_args: list[str]
	fail_command: list[FailCommand]
	dependencies: list[str]
