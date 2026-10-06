# A context-aware callable misses a value assigned in a loop

## Reproduction

Save this script as `repro.py` in the repository root, then run `python repro.py`.

```python
from jinja2 import Environment, pass_context


@pass_context
def current_value(context):
    return context.get("value", "missing")


env = Environment(autoescape=False)
env.globals["current_value"] = current_value
template = env.from_string(
    "{% set value='outer' %}{{ current_value() }}|"
    "{% for item in ['x'] %}{% set value='inner' %}"
    "{{ current_value() }}{% endfor %}|{{ current_value() }}"
)
print(template.render())
```

## Expected behavior

The callable sees the loop's `inner` assignment during the iteration, while the outer value remains `outer` before and after the loop. Output: `outer|inner|outer`.

## Observed behavior

The call inside the loop sees the unchanged outer value. Output: `outer|outer|outer`.

## Focused check

```sh
python -m pytest -q tests/test_bugsquash.py -k context_callable_sees_loop
```
