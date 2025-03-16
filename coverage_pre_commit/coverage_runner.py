import argparse
from collections.abc import Sequence

from coverage_pre_commit.common.enums import Providers


def main(argv: Sequence[str] | None = None) -> int:  # noqa: D103
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"provider",
		default=Providers.UNITTEST.value,
		choices=[provider.value for provider in Providers],
	)
	args = parser.parse_args(argv)

	return args


if __name__ == "__main__":
	raise SystemExit(main())
