import subprocess
import sys


def check_dependencies(dependencies: list[str]) -> None:
	for dependency in dependencies:
		try:
			subprocess.check_output([sys.executable, "-m", "pip", "show", dependency], stderr=subprocess.DEVNULL)
		except subprocess.CalledProcessError:
			subprocess.check_call([sys.executable, "-m", "pip", "install", dependency], stdout=subprocess.DEVNULL)
