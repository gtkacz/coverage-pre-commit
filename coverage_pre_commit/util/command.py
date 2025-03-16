import re
import subprocess
from argparse import Namespace

from coverage_pre_commit.common.types import ProviderValue


def build_command(provider: ProviderValue, args: Namespace) -> str:
	command = provider["command"]

	if args.args:
		command += " " + " ".join(args.args)

	if not provider["fail_command"]["is_arg"]:
		command += " && " + provider["fail_command"]["command"].format(args.fail_under[0])
	else:
		command += provider["fail_command"]["command"].format(args.fail_under[0])

	command = re.sub(r"\s{2,}", " ", command)

	return command.strip()


def execute_command(command: str) -> int:
	"""
	Execute a command using subprocess.run.

	Args:
		command (str): The command to execute.

	Returns:
		int: The return code of the command.
	"""
	return (
		subprocess.run(
			command,
			shell=True,
			check=False,
			stdout=subprocess.DEVNULL,
			stderr=subprocess.STDOUT,
		).check_returncode()
		or 1
	)
