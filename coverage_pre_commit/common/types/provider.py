from typing import List, TypedDict


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
	default_args: List[str]
	fail_command: List[FailCommand]
	dependencies: List[str]
