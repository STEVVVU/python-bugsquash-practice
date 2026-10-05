# Choice value preservation

For a case-insensitive `Choice`, matching input may use different letter case
from a configured choice. The result should still be the original configured
choice, so applications that use those values receive their declared value.

Copy this snippet into `repro.py` at the repository root, then run
`python repro.py`:

```python
import click
from click.testing import CliRunner


choice = click.Choice(["json", "yaml"], case_sensitive=False)
command = click.Command(
    "app",
    params=[click.Argument(["format"], type=choice)],
    callback=lambda format: format,
)
result = CliRunner().invoke(command, ["JSON"], standalone_mode=False)
print(result.return_value)
```

Expected: `json`. The starter returns `JSON`.

Focused test:

```console
python -m pytest tests/test_types.py -k choice_case_insensitive_value_returns_original_choice
```

Case-sensitive choice behavior and invalid-choice reporting should remain intact.
