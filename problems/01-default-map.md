# Parameter source for false-like configuration

When a command receives a false-like value from its `default_map`, Click should
report its source as `DEFAULT_MAP`, just as it does for truthy values. The
configured value is used; the issue is that callers inspecting its origin can
receive the wrong source.

Copy this snippet into `repro.py` at the repository root, then run
`python repro.py`:

```python
import click
from click.testing import CliRunner


def report_source(ctx, param, value):
    return value, ctx.get_parameter_source("limit").name


option = click.Option(["--limit"], default=5, callback=report_source)
command = click.Command("app", params=[option], callback=lambda limit: limit)
result = CliRunner().invoke(
    command, [], default_map={"limit": 0}, standalone_mode=False
)
print(result.return_value)
```

Expected: `(0, 'DEFAULT_MAP')`. The starter reports `(0, 'DEFAULT')`.

Focused test:

```console
python -m pytest tests/test_defaults.py -k 'falsey_default_map_value_reports_default_map_source or missing_default_map_key'
```

The neighboring absent-key case should continue to use the option's own default
and report `DEFAULT`.
