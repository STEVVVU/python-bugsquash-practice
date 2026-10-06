# Nested autoescape state is not restored

## Reproduction

Save this script as `repro.py` in the repository root, then run `python repro.py`.

```python
from jinja2 import Environment, pass_eval_context


@pass_eval_context
def autoescape_state(eval_ctx, value):
    return str(eval_ctx.autoescape)


env = Environment(autoescape=False)
env.filters["autoescape_state"] = autoescape_state
template = env.from_string(
    "{% autoescape true %}{{ value|autoescape_state }}|"
    "{% autoescape false %}{{ value|autoescape_state }}"
    "{% endautoescape %}|{{ value|autoescape_state }}"
    "{% endautoescape %}|{{ value|autoescape_state }}"
)
print(template.render(value="x"))
```

## Expected behavior

The filter observes the active state at each point: `True|False|True|False`.

## Observed behavior

The inner `false` setting remains active after its scope ends, so the filter reports `True|False|False|False`.

## Focused check

```sh
python -m pytest -q tests/test_bugsquash.py -k nested_autoescape
```
