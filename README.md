# coverage-pre-commit

A pre-commit hook to run coverage on your code and enforce a minimum coverage threshold.

## Features

* **Multiple Test Providers**: Supports both unittest and pytest, with the ability to add custom providers
* **Flexible Configuration**: Customize coverage thresholds, test command arguments, and more
* **Dependency Management**: Automatically checks and installs required dependencies
* **Pre-commit Integration**: Works seamlessly with pre-commit hooks

## Installation

```console
$ pip install coverage-pre-commit
```

## Usage

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/gtkacz/coverage-pre-commit
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    -   id: coverage-pre-commit
        args: [--fail-under=80]  # Set your desired coverage threshold
```

### Command Line Options

```console
$ coverage_pre_commit --help
usage: coverage_runner.py [-h] [--version] [--provider PROVIDER] [--args ARGS]
                         [--fail-under FAIL_UNDER]
                         [--extra-dependencies EXTRA_DEPENDENCIES]
                         [--command COMMAND]

Run tests with coverage and verify coverage thresholds

options:
  -h, --help            show this help message and exit
  --version             Show version information
  --provider PROVIDER   Test provider (unittest, pytest, or custom)
  --args ARGS           Additional arguments to pass to the test command
  --fail-under FAIL_UNDER
                        Minimum coverage percentage to fail the build
  --extra-dependencies EXTRA_DEPENDENCIES
                        Additional dependencies to install
  --command COMMAND     Custom command to run tests (required if provider is not supported)
```

### Example Usage

#### With unittest

```console
$ coverage_pre_commit --provider unittest --fail-under 80
```

#### With pytest

```console
$ coverage_pre_commit --provider pytest --fail-under 90
```

#### With custom command

```console
$ coverage_pre_commit --command "custom test command" --fail-under 85
```

## Supported Providers

- **unittest**: Uses Python's built-in unittest framework with coverage
- **pytest**: Uses pytest with pytest-cov plugin
- **custom**: Allows specifying a custom test command

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/gtkacz/coverage-pre-commit/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gtkacz/coverage-pre-commit" alt="contrib.rocks image" />
</a>

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Gabriel Mitelman Tkacz - [@gtkacz](https://github.com/gtkacz) - gmtkacz@proton.me

Project Link: [https://github.com/gtkacz/coverage-pre-commit](https://github.com/gtkacz/coverage-pre-commit)
