<div align="center"><img src="https://raw.githubusercontent.com/pallets/click/refs/heads/stable/docs/_static/click-name.svg" alt="" height="150"></div>

# Click

## Bugsquash Practice

This repository contains three independent Click behavior exercises. The starter
has three independent seeded bugs that produce 16 failing pytest cases. Use the
reports in [`problems/`](problems/) to reproduce each behavior and run its
focused test. With all three behaviors repaired, the suite has 1,913 passing
tests, plus the unchanged skips, expected failure, and stress-test deselections.

Requires Python 3.11. From the repository root, create an environment and install
the package and its pinned test dependency:

```console
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -e . -r requirements-dev.txt
```

Run the full suite with `python -m pytest`. The 16 starter failures all arise
from the three reported behavior boundaries; the remaining upstream suite
continues to pass. Focused commands and expected results are listed in each
problem report.

The exercise is based on Pallets Click 8.5.0. See [`UPSTREAM.md`](UPSTREAM.md)
for source attribution and packaging notes.

---

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

Click in three points:

-   Arbitrary nesting of commands
-   Automatic help page generation
-   Supports lazy loading of subcommands at runtime


## A Simple Example

```python
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
```

```
$ python hello.py --count=3
Your name: Click
Hello, Click!
Hello, Click!
Hello, Click!
```


## Donate

The Pallets organization develops and supports Click and other popular
packages. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today][].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/
