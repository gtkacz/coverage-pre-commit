import subprocess
import sys
from typing import List


def check_dependencies(dependencies: List[str]) -> None:
	"""
	Check if the dependencies are installed, if not install them.

	Args:
		dependencies (list[str]): List of dependencies to check and install.
	"""
	for dependency in dependencies:
		try:
			subprocess.check_output([sys.executable, "-m", "pip", "show", dependency], stderr=subprocess.DEVNULL)
		except subprocess.CalledProcessError:
			subprocess.check_call([sys.executable, "-m", "pip", "install", dependency], stdout=subprocess.DEVNULL)
