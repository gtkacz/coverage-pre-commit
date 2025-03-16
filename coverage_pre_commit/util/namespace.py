from __future__ import annotations

import argparse

EMPTY_NAMESPACE = argparse.Namespace(
	version=False,
	provider=["unittest"],
	args=[""],
	fail_under=None,
	extra_dependencies=None,
	command=None,
)
