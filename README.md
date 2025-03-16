# Python CLI Template

## Features

* **Short & Easy**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Docker-Ready**: Dockerfile included, with one make command you can build and deploy it to ecr.
* **Comes With Pre-made Commands**: Available Make commands to build, deploy and clean the images.


## Installation

```console
$ cookiecutter https://github.com/talperetz/python-cli-template
```

```console
$ pip install -r requirements.txt
```

## Usage

1. Edit [command_name].py file to execute your desired commands
2. make build
3. make ecrpush

### Run it

Run your application:


```console
// Run your application
$ python [command_name].py

// You get a nice error, you are missing NAME
Usage: main.py [OPTIONS] NAME
Try "main.py --help" for help.

Error: Missing argument "NAME".

// You get a --help for free
$ python main.py --help

Usage: [command_name].py [OPTIONS] NAME

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

// You get ✨ auto completion ✨ for free, installed with --install-completion

// Now pass the NAME argument
$ python [command_name].py Camila

Hello Camila

// It works! 🎉
```

## Optional Dependencies

Typer uses <a href="https://click.palletsprojects.com/" class="external-link" target="_blank">Click</a> internally. That's the only dependency.

But you can also install extras:

* <a href="https://pypi.org/project/colorama/" class="external-link" target="_blank"><code>colorama</code></a>: and Click will automatically use it to make sure your terminal's colors always work correctly, even in Windows.
    * Then you can use any tool you want to output your terminal's colors in all the systems, including the integrated `typer.style()` and `typer.secho()` (provided by Click).
    * Or any other tool, e.g. <a href="https://pypi.org/project/wasabi/" class="external-link" target="_blank"><code>wasabi</code></a>, <a href="https://github.com/erikrose/blessings" class="external-link" target="_blank"><code>blessings</code></a>.
* <a href="https://github.com/click-contrib/click-completion" class="external-link" target="_blank"><code>click-completion</code></a>: and Typer will automatically configure it to provide completion for all the shells, including installation commands.

You can install `typer` with `colorama` and `click-completion` with `pip install typer[all]`.

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

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)
