# An inherited block loses access to the active loop

## Reproduction

Save this script as `repro.py` in the repository root, then run `python repro.py`.

```python
from jinja2 import DictLoader, Environment

env = Environment(
    loader=DictLoader(
        {
            "base.html": (
                "{% for item in items %}{% block card scoped %}"
                "base{% endblock %}{% endfor %}"
            ),
            "child.html": (
                "{% extends 'base.html' %}{% block card %}"
                "{{ loop.index }}={{ item }};{% endblock %}"
            ),
        }
    )
)
print(env.get_template("child.html").render(items=["a", "b"]))
```

## Expected behavior

The child override can read the current item and loop index and renders `1=a;2=b;`.

## Observed behavior

Rendering raises `jinja2.exceptions.UndefinedError: 'loop' is undefined`.

## Focused check

```sh
python -m pytest -q tests/test_bugsquash.py -k inherited_override
```
