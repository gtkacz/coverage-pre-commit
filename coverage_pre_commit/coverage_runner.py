import argparse
from collections.abc import Sequence

from coverage_pre_commit.common.enums import Providers
from coverage_pre_commit.util import check_dependencies, execute_command


def main(argv: Sequence[str] | None = None) -> int:  # noqa: D103
	try:
		provider = Providers.UNITTEST.value

		parser = argparse.ArgumentParser()

		parser.add_argument(
			"--provider",
			default=provider["name"],
			nargs=1,
		)

		parser.add_argument(
			"--args",
			required=False,
			nargs=1,
		)

		parser.add_argument(
			"--fail-under",
			required=True,
			help="Minimum coverage percentage to fail the build",
			nargs=1,
		)

		parser.add_argument(
			"--extra-dependencies",
			required=False,
			nargs=1,
		)

		parser.add_argument(
			"--command",
			required=False,
			nargs=1,
		)

		args = parser.parse_args(argv)

		if args.provider[0].upper() in Providers.names:
			provider = Providers[args.provider[0]].value

			check_dependencies(provider["dependencies"])

			args.provider = provider["name"]
			args.args = provider["default_args"]

		elif not args.command[0]:
			raise RuntimeError(
				f"If you are using an unsupported provider, you must also provide a command.\nYour provider was: {args.provider[0]}\nSupported providers are: {list(map(str.lower, Providers.names))}",
			)

		if args.extra_dependencies[0]:
			check_dependencies(args.extra_dependencies[0].split(","))

		if args.command[0]:
			return execute_command(args.command[0])

		if not args.args:
			args.args = "".join(args.args)

		command = f"{provider['command']} {args.args} {'&& ' if not provider['fail_command']['is_arg'] else ''}{provider['fail_command']['command'].format(args.fail_under[0])}"
		return execute_command(command)

	except Exception as e:
		print(e)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
