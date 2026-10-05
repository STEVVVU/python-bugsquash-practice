# Optional filesystem paths

`Path` accepts paths that do not exist when `exists=False` (the default). When
`path_type` is provided, the result should use that requested path type whether
or not the target currently exists.

Copy this snippet into `repro.py` at the repository root, then run
`python repro.py`:

```python
import pathlib

import click
from click.testing import CliRunner


path_type = click.Path(path_type=pathlib.Path)
command = click.Command(
    "app",
    params=[click.Argument(["path"], type=path_type)],
    callback=lambda path: path,
)
result = CliRunner().invoke(
    command, ["__click_optional_missing_path__"], standalone_mode=False
)
value = result.return_value
print(type(value).__name__, value)
```

Expected: `PosixPath __click_optional_missing_path__` on macOS/Linux or
`WindowsPath __click_optional_missing_path__` on Windows. The starter returns a
`str` instead.

Focused test:

```console
python -m pytest tests/test_types.py -k path_type_is_applied_to_missing_path
```

The default string result and path validation for existing paths should remain
unchanged.
