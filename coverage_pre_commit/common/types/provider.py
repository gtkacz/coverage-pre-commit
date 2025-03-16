from typing import List, TypedDict


class FailCommand(TypedDict):
	command: str
	is_arg: bool


class ProviderValue(TypedDict):
	name: str
	command: str
	default_args: List[str]
	fail_command: List[FailCommand]
	dependencies: List[str]
