import argparse
import sys
import traceback
from typing import Optional, Sequence

from coverage_pre_commit.common.enums import Providers
from coverage_pre_commit.util import EMPTY_NAMESPACE, build_command, check_dependencies, execute_command, get_metadata


def main(argv: Optional[Sequence[str]] = None) -> None:  # noqa: D103
	available_providers = list(map(str.lower, Providers.names))
	provider = Providers.UNITTEST.value

	try:
		parser = argparse.ArgumentParser(description="Run tests with coverage and verify coverage thresholds")

		parser.add_argument(
			"--version",
			help="Show version information",
			action="store_true",
		)

		parser.add_argument(
			"--provider",
			type=str,
			default=[provider["name"]],
			help=f"Test provider ({''.join(available_providers)}, or custom)",
			nargs=1,
		)

		parser.add_argument(
			"--args",
			type=str,
			default=[""],
			help="Additional arguments to pass to the test command",
			nargs=1,
		)

		parser.add_argument(
			"--fail-under",
			type=float,
			required=False,
			help="Minimum coverage percentage to fail the build",
			nargs=1,
		)

		parser.add_argument(
			"--extra-dependencies",
			type=str,
			required=False,
			nargs=1,
		)

		parser.add_argument(
			"--command",
			type=str,
			required=False,
			help="Custom command to run tests (required if provider is not supported)",
			nargs=1,
		)

		args = parser.parse_args(argv)

		if args == EMPTY_NAMESPACE:
			parser.print_help()
			sys.exit(0)

		if args.version:
			print(f"coverage_pre_commit {get_metadata('version')}")  # noqa: T201
			sys.exit(0)

		elif not args.fail_under or (args.fail_under[0] < 0 or args.fail_under[0] > 100):  # noqa: PLR2004
			raise RuntimeError("The fail-under argument must be passed and must be between 0 and 100.")

		if args.provider[0].upper() not in Providers.names and not args.command:
			raise RuntimeError(
				"If you are using an unsupported provider, you must also provide a command.\n"
				f"Your provider was: {args.provider[0]}\n"
				f"Supported providers are: {available_providers}",
			)

		if args.extra_dependencies:
			check_dependencies(args.extra_dependencies[0].split(","))

		if args.command:
			sys.exit(execute_command(args.command[0]))

		provider = Providers[args.provider[0].upper()].value

		check_dependencies(provider["dependencies"])

		args.provider = provider["name"]
		args.args = (provider["default_args"] or []) + (args.args or [])

		sys.exit(execute_command(build_command(provider, args)))

	except Exception as e:
		traceback.print_exception(type(e), e, e.__traceback__)
		sys.exit(1)


if __name__ == "__main__":
	raise SystemExit(main())
