import subprocess


def execute_command(command: str) -> int:
	"""
	Execute a command using subprocess.run.

	Args:
	    command (str): The command to execute.

	Returns:
	    int: The return code of the command.
	"""
	return subprocess.run(command, shell=True, check=False).returncode
